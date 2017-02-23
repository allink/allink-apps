# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from django.db import models

from adminsortable.fields import SortableForeignKey
from parler.models import TranslatableModel, TranslatedFields
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PlaceholderField
from model_utils.models import TimeFramedModel

from aldryn_translation_tools.models import (
    TranslatedAutoSlugifyMixin,
    TranslationHelperMixin,
)
from aldryn_common.admin_fields.sortedm2m import SortedM2MModelField

from allink_core.allink_categories.models import AllinkCategory
from allink_core.allink_base.models.mixins import AllinkManualEntriesMixin
from allink_core.allink_base.models.managers import AllinkBaseModelManager
from allink_core.allink_base.models import AllinkBaseModel, AllinkBaseImage, AllinkBaseAppContentPlugin, AllinkBaseRegistration
from allink_core.allink_terms.models import AllinkTerms
from allink_apps.locations.models import Locations

from .managers import AllinkEventsManager


#  Blog Parent class
class Blog(TranslationHelperMixin, TranslatedAutoSlugifyMixin, TranslatableModel, TimeFramedModel, AllinkBaseModel):
    """
    Translations
     feel free to add app specific fields)
     to override slug generation:
     slug_source_field_name = 'title'

    """
    slug_source_field_name = 'title'

    translations = TranslatedFields(
        title=models.CharField(
            max_length=255
        ),
        slug=models.SlugField(
            _(u'Slug'),
            max_length=255,
            default='',
            blank=True,
            help_text=_(u'Leave blank to auto-generate a unique slug.')
        ),
        lead=HTMLField(
            _(u'Lead Text'),
            help_text=_(u'Teaser text that in some cases is used in the list view and/or in the detail view.'),
            blank=True,
            null=True,
        ),
        text=HTMLField(
            _(u'Detailed Text'),
            help_text=_(u'The full text in detail view.'),
            blank=True,
            null=True,
        )
    )

    header_placeholder = PlaceholderField(u'blog_header', related_name='header_placeholder')
    content_placeholder = PlaceholderField(u'blog_content', related_name='content_placeholder')

    objects = AllinkBaseModelManager()

    class Meta:
        app_label = 'blog'
        verbose_name = _('Blog entry')
        verbose_name_plural = _('Blog entries')

    @property
    def preview_image(self):
        if self.blogimage_set.count() > 0:
            return self.blogimage_set.first().image

    @property
    def images(self):
        return self.blogimage_set.all()


# News
class News(Blog):

    objects = AllinkBaseModelManager()

    class Meta:
        app_label = 'blog'
        verbose_name = _('News entry')
        verbose_name_plural = _('News')

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        app = 'blog:detail'.format(self._meta.model_name)
        return reverse(app, kwargs={'slug': self.slug})


# Events
class Events(Blog):

    objects = AllinkEventsManager()

    translations_events = TranslatedFields(
        costs=models.CharField(
            max_length=255,
            help_text=_(u'Costs'),
            blank=True,
            null=True,
        )
    )

    form_enabled = models.BooleanField(
        _(u'Event Form enabled'),
        default=True
    )

    event_date = models.DateField(
        _(u'Event Date'),
        blank=True,
        null=True,
    )

    event_time = models.TimeField(
        _(u'Event Time'),
        blank=True,
        null=True,
    )

    location = models.ForeignKey(
        Locations,
        blank=True,
        null=True,
        related_name='events'
    )

    class Meta:
        app_label = 'blog'
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        app = 'blog:detail'.format(self._meta.model_name)
        return reverse(app, kwargs={'slug': self.slug})


# APP CONTENT PLUGIN
class BlogAppContentPlugin(AllinkManualEntriesMixin, AllinkBaseAppContentPlugin):
    """
    """

    TEMPLATES = (
        (AllinkBaseAppContentPlugin.GRID_STATIC, 'Grid (Static)'),
        (AllinkBaseAppContentPlugin.SLIDER, 'Slider'),
    )

    data_model = Blog

    manual_entries = SortedM2MModelField(
        '{}.{}'.format(data_model._meta.app_label, data_model._meta.model_name), blank=True,
        help_text=_('Select and arrange specific entries, or, leave blank to select all. (If '
                    'manual entries are selected the category filtering will be ignored.)')
    )

    # def get_specific_model(self, category):
    #     if category.name == 'News':
    #         return News
    #     elif category.name == 'Events':
    #         return Events
    #     else:
    #         return Blog
    #
    # def get_render_queryset_for_display(self, category=None, category_id=None):
    #     """
    #      returns all data_model objects distinct to id which are in the selected categories
    #      - either use category or category_id to select specific entries
    #      -if neither category nor category_id is supplied
    #
    #     """
    #     cat = None
    #
    #     if self.categories.count() > 0:
    #         """
    #          category selection
    #         """
    #         # performance enhancement when only one category
    #         # if category_id is supplied, this one should be use
    #         # if categories count == 1 this one should be used
    #         if category:
    #             cat = category
    #         elif category_id:
    #             cat = AllinkCategory.objects.get(id=category_id)
    #         elif self.categories.count == 1:
    #             cat = self.categories.select_related().first()
    #
    #         if cat:
    #             # TODO how donwcasting to specific model??
    #             queryset = self.get_specific_model(cat).objects.filter_by_category(cat)
    #
    #         else:
    #             # more than one category on the same page
    #             # because we have different models in Blog, we also have different instances here
    #             queryset = self.data_model.objects.filter_by_categories(self.categories).select_subclasses(News, Events)
    #
    #         return self._apply_ordering_to_queryset_for_display(queryset)
    #
    #     else:
    #         """
    #          manual entries
    #          ordering is always like manual entries order (drag n drop)
    #          resulting instances are alwas blog entries because we can't downcast and order
    #         """
    #         queryset = self.manual_entries.select_related()
    #
    #         return queryset


class BlogImage(AllinkBaseImage):
    blog = SortableForeignKey(Blog, verbose_name=_(u'Images'), help_text=_(u'The first image will be used as preview image.'), blank=True, null=True)


class EventsRegistration(AllinkBaseRegistration):

    event = models.ForeignKey(Events)

    job = models.TextField(
        _(u'Education/ Job')
    )
    terms = models.ForeignKey(
        AllinkTerms,
        verbose_name=_(u'Terms')
    )
