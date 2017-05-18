# -*- coding: utf-8 -*-
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.db import models

from filer.fields.image import FilerImageField
from adminsortable.fields import SortableForeignKey
from parler.models import TranslatableModel, TranslatedFields
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PlaceholderField
from model_utils.models import TimeFramedModel

from aldryn_translation_tools.models import TranslationHelperMixin
from aldryn_common.admin_fields.sortedm2m import SortedM2MModelField

from allink_core.allink_base.models.choices import SALUTATION_CHOICES
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

    preview_image = FilerImageField(
        verbose_name=_(u'Preview Image'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_preview_image',
    )

    template = models.CharField(
        _(u'Template'),
        help_text=_(u'Choose a template.'),
        max_length=50,
        blank=True,
        null=True,
    )

    header_placeholder = PlaceholderField(u'blog_header', related_name='%(app_label)s_%(class)s_header_placeholder')
    content_placeholder = PlaceholderField(u'blog_content', related_name='%(app_label)s_%(class)s_content_placeholder')

    objects = AllinkBlogManager()

    class Meta:
        app_label = 'blog'
        verbose_name = _('Blog entry')
        verbose_name_plural = _('Blog entries')

    def get_detail_view(self):
        return 'blog:detail'.format(self._meta.model_name)

# News
class News(Blog):
    objects = AllinkBlogManager()

    class Meta:
        app_label = 'blog'
        verbose_name = _('News entry')
        verbose_name_plural = _('News')

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

    def __str__(self):
        return u'%s %s' % (self.title, self.event_date)

    def show_registration_form(self):
        if getattr(self, 'event_date'):
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

        def ordered_by_events():
            if category and getattr(category, 'name') == 'Events':
                return True
            elif self.categories.count() == 1 and self.categories.first().name == 'Events':
                return True
            else:
                return False

        # apply filters from request
        queryset = self.data_model.objects.active().filter(**filters)

        if self.categories.exists() or category:
            if category:
                #  TODO how can we automatically apply the manager of the subclass?
                if ordered_by_events():
                    queryset = Events.objects.active().filter_by_category(category)
                else:
                    queryset = queryset.filter_by_category(category)
            else:
                if ordered_by_events():
                    queryset = Events.objects.active().filter_by_categories(categories=self.categories.all())
                else:
                    queryset = queryset.filter_by_categories(categories=self.categories.all())

            if self.categories_and.exists():
                queryset = queryset.filter_by_categories(categories=self.categories_and.all())

        return self._apply_ordering_to_queryset_for_display(queryset)



class BlogImage(AllinkBaseImage):
    blog = SortableForeignKey(Blog, verbose_name=_(u'Images'), help_text=_(u'The first image will be used as preview image.'), blank=True, null=True)


class EventsRegistration(AllinkAddressFieldsModel, AllinkSimpleRegistrationFieldsModel):

    require_terms = False

    event = models.ForeignKey(Events)

    # job = models.TextField(
    #     _(u'Education/ Job')
    # )

    salutation = models.IntegerField(
        _(u'Salutation'),
        choices=SALUTATION_CHOICES,
        null=True
    )
    company_name = models.CharField(
        _(u'Company'),
        max_length=255,
        blank=True,
        null=True
    )
    phone = models.CharField(
        _(u'Phone'),
        max_length=30,
        blank=True,
        null=True
    )

    # terms = models.ForeignKey(
    #     AllinkTerms,
    #     verbose_name=_(u'I have read and accept the terms and conditions.'),
    #     null=True
    # )

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    @classmethod
    def get_verbose_name(cls):
        from allink_core.allink_config.models import AllinkConfig
        try:
            field_name = cls._meta.model_name + '_verbose'
            return getattr(AllinkConfig.get_solo(), field_name)
        except AttributeError:
            return cls._meta.verbose_name

    @classmethod
    def get_verbose_name_plural(cls):
        from allink_core.allink_config.models import AllinkConfig
        try:
            field_name = cls._meta.model_name + '_verbose_plural'
            return getattr(AllinkConfig.get_solo(), field_name)
        except AttributeError:
            return cls._meta.verbose_name_plural
