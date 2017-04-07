# -*- coding: utf-8 -*-
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

from django.db import models

from adminsortable.fields import SortableForeignKey
from parler.models import TranslatableModel, TranslatedFields
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PlaceholderField
from model_utils.models import TimeFramedModel

from aldryn_translation_tools.models import TranslationHelperMixin
from aldryn_common.admin_fields.sortedm2m import SortedM2MModelField

from allink_core.allink_base.models import AllinkManualEntriesMixin, AllinkTranslatedAutoSlugifyMixin
from allink_core.allink_base.models import AllinkBaseModel, AllinkBaseImage, AllinkBaseAppContentPlugin, AllinkAddressFieldsModel, AllinkSimpleRegistrationFieldsModel
from allink_core.allink_terms.models import AllinkTerms
from allink_apps.locations.models import Locations

from polymorphic.models import PolymorphicModel

from allink_apps.blog.managers import AllinkEventsManager, AllinkBlogManager


#  Blog Parent class
class Blog(PolymorphicModel, TranslationHelperMixin, AllinkTranslatedAutoSlugifyMixin, TranslatableModel, TimeFramedModel, AllinkBaseModel):
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

    header_placeholder = PlaceholderField(u'blog_header', related_name='%(app_label)s_%(class)s_header_placeholder')
    content_placeholder = PlaceholderField(u'blog_content', related_name='%(app_label)s_%(class)s_content_placeholder')

    objects = AllinkBlogManager()

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
    objects = AllinkBlogManager()

    class Meta:
        app_label = 'blog'
        verbose_name = _('News entry')
        verbose_name_plural = _('News')

    def get_detail_view(self):
        'blog:detail'.format(self._meta.model_name)


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

    def get_detail_view(self):
        'blog:detail'.format(self._meta.model_name)

    def show_registration_form(self):
        if self.event_date < datetime.now().date():
            return False
        if self.form_enabled:
            return True
        else:
            return False


# APP CONTENT PLUGIN
class BlogAppContentPlugin(AllinkManualEntriesMixin, AllinkBaseAppContentPlugin):

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

    def get_render_queryset_for_display(self, category=None, filters={}):
        """
         returns all data_model objects distinct to id which are in the selected categories
          - category: category instance
          - filter: list tuple with model fields and value
            -> adds additional query

        -> Is also defined in  AllinkManualEntriesMixin to handel manual entries !!
        """

        # apply filters from request
        queryset = self.data_model.objects.filter(**filters)

        if self.categories.count() > 0 or category:
            """
             category selection
            """
            if category:
                #  TODO how can we automatically apply the manager of the subclass?
                if category.name == 'Events':
                    queryset = Events.objects.filter_by_category(category)
                    if self.categories_and.count() > 0:
                        queryset = queryset.filter(categories=self.categories_and.all())
                else:
                    queryset = self.data_model.objects.filter_by_category(category)
                    if self.categories_and.count() > 0:
                        queryset = queryset.filter(categories=self.categories_and.all())
            else:
                queryset = self.data_model.objects.filter_by_categories(self.categories)
                if self.categories_and.count() > 0:
                    queryset = queryset.filter(categories=self.categories_and.all())

            return self._apply_ordering_to_queryset_for_display(queryset)

        else:
            queryset = self.data_model.objects.active()
            return queryset


class BlogImage(AllinkBaseImage):
    blog = SortableForeignKey(Blog, verbose_name=_(u'Images'), help_text=_(u'The first image will be used as preview image.'), blank=True, null=True)


class EventsRegistration(AllinkAddressFieldsModel, AllinkSimpleRegistrationFieldsModel):

    event = models.ForeignKey(Events)

    job = models.TextField(
        _(u'Education/ Job')
    )
    terms = models.ForeignKey(
        AllinkTerms,
        verbose_name=_(u'I have read and accept the terms and conditions.'),
        null=True
    )
