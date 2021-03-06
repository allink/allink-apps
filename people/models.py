# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from cms.models.fields import PlaceholderField
from adminsortable.fields import SortableForeignKey
from parler.models import TranslatableModel, TranslatedFields
from aldryn_translation_tools.models import TranslationHelperMixin
from aldryn_common.admin_fields.sortedm2m import SortedM2MModelField

from allink_core.allink_base.models.choices import GENDER_CHOICES
from allink_core.allink_base.models import AllinkManualEntriesMixin, AllinkTranslatedAutoSlugifyMixin, AllinkContactFieldsModel
from allink_core.allink_base.models import AllinkBaseModel, AllinkBaseImage, AllinkBaseAppContentPlugin, AllinkAddressFieldsModel

from allink_apps.people.managers import AllinkPeopleManager


class People(TranslationHelperMixin, AllinkTranslatedAutoSlugifyMixin, TranslatableModel, AllinkContactFieldsModel, AllinkAddressFieldsModel, AllinkBaseModel):
    """
    Translations
     feel free to add app specific fields)
     to override slug generation:
     slug_source_field_name = 'full_name'

    """
    slug_source_field_name = 'full_name'

    firstname = models.CharField(
        _(u'Firstname'),
        max_length=255,
        default=''
    )
    lastname = models.CharField(
        _(u'Lastname'),
        max_length=255,
        default=''
    )
    preview_image = FilerImageField(
        verbose_name=_(u'Preview Image'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_preview_image',
    )

    translations = TranslatedFields(
        # to be removed in release 0.0.8, or when all old projects are up to date
        old_firstname=models.CharField(
            _(u'Firstname'),
            max_length=255,
            default=''
        ),
        # to be removed in release 0.0.8, or when all old projects are up to date
        old_lastname=models.CharField(
            _(u'Lastname'),
            max_length=255,
            default=''
        ),
        job_title=models.CharField(
            _(u'Unit'),
            max_length=255,
            default=''
        ),
        job_function=models.CharField(
            _(u'Function'),
            max_length=255,
            default=''
        ),
        text=HTMLField(
            _(u'Text'),
            blank=True,
            null=True
        ),
        slug=models.SlugField(
            _(u'Slug'),
            max_length=255,
            default='',
            blank=True,
            help_text=_(u'Leave blank to auto-generate a unique slug.')
        ),
    )

    company_name = models.CharField(
        _(u'Company Name'),
        max_length=255,
        blank=True,
        null=True
    )

    gender = models.IntegerField(
        _(u'Gender'),
        choices=GENDER_CHOICES,
        null=True
    )

    header_placeholder = PlaceholderField(u'people_header', related_name='%(app_label)s_%(class)s_header_placeholder')
    content_placeholder = PlaceholderField(u'people_content', related_name='%(app_label)s_%(class)s_content_placeholder')

    objects = AllinkPeopleManager()

    class Meta:
        app_label = 'people'
        verbose_name = _('Person')
        verbose_name_plural = _('People')

    @property
    def full_name(self):
        return u'{} {}'.format(self.firstname, self.lastname)

    @property
    def title(self):
        return u'{} {}'.format(self.firstname, self.lastname)

    @property
    def units(self):
        units = []
        for unit in self.categories.filter(identifier='units'):
            units.append(unit.name)
        return ','.join(units)


# APP CONTENT PLUGIN
class PeopleAppContentPlugin(AllinkManualEntriesMixin, AllinkBaseAppContentPlugin):
    """
    specify:

    data_model = People

    manual_entries = SortedM2MModelField(
        People, blank=True,
        help_text=_('Select and arrange specific entries, or, leave blank to select all. (If '
                    'manual entries are selected, the category filtering is not active.)')
    )

    """


    FILTER_FIELD_CHOICES = (
        ('categories', {
            'verbose': _(u'Unit'),
            'query_filter': {'identifier': 'units'},
        }),
        # at the moment we can't handle two different categories at the same time
        # ('categories', {
        #     'verbose': _(u'Location'),
        #     'query_filter': {'tag': 'locations'},
        #     # if locations have not been generated automatically
        #     # PROJECT_CATEGORY_IDENTIFIERS has to be set in settings accordingly ()
        #     # 'query_filter': {'identifier': 'locations'},
        # }),
        ('job_function', {
            'verbose': _(u'Job Function'),
            'query_filter': {},
        }),
        ('lastname', {
            'verbose': _(u'Lastname'),
            'query_filter': {},
        }),
        ('job_title', {
            'verbose': _(u'Job Title'),
            'query_filter': {},
        }),
    )

    data_model = People

    manual_entries = SortedM2MModelField(
        '{}.{}'.format(data_model._meta.app_label, data_model._meta.model_name), blank=True,
        help_text=_('Select and arrange specific entries, or, leave blank to select all. (If '
                    'manual entries are selected the category filtering will be ignored.)')
    )


class PeopleImage(AllinkBaseImage):
    people = SortableForeignKey(People, verbose_name=_(u'Images'), help_text=_(u'The first image will be used as preview image.'), blank=True, null=True)
