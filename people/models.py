# -*- coding: utf-8 -*-
import phonenumbers
from django.utils.translation import ugettext_lazy as _
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from adminsortable.fields import SortableForeignKey
from parler.models import TranslatableModel, TranslatedFields
from aldryn_translation_tools.models import (
    TranslatedAutoSlugifyMixin,
    TranslationHelperMixin,
)
from aldryn_common.admin_fields.sortedm2m import SortedM2MModelField

from allink_core.allink_base.models.choices import GENDER_CHOICES
from allink_core.allink_base.models.mixins import AllinkManualEntriesMixin
from allink_core.allink_base.models import AllinkBaseModel, AllinkBaseImage, AllinkBaseAppContentPlugin, AllinkContactFieldsModel, AllinkAddressBasicFieldsModel

from .managers import AllinkPeopleManager


class People(TranslationHelperMixin, TranslatedAutoSlugifyMixin, TranslatableModel, AllinkContactFieldsModel, AllinkAddressBasicFieldsModel, AllinkBaseModel):
    """
    Translations
     feel free to add app specific fields)
     to override slug generation:
     slug_source_field_name = 'full_name'

    """


    slug_source_field_name = 'full_name'

    translations = TranslatedFields(
        firstname=models.CharField(
            _(u'Firstname'),
            max_length=255,
            default=''
        ),
        lastname=models.CharField(
            _(u'Lastname'),
            max_length=255,
            default=''
        ),
        job_title=models.CharField(
            _(u'Job Title'),
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

    # location = models.ManyToManyField(Locations, blank=True, null=True, related_name='people')

    objects = AllinkPeopleManager()

    class Meta:
        app_label = 'people'
        verbose_name = _('Person')
        verbose_name_plural = _('People')

    @property
    def full_name(self):
        return u'{} {}'.format(self.firstname, self.lastname)

    @property
    def preview_image(self):
        if self.peopleimage_set.count() > 0:
            return self.peopleimage_set.first().image

    @property
    def images(self):
        return self.peopleimage_set.all()

    @property
    def title(self):
        return u'{} {}'.format(self.firstname, self.lastname)


# APP CONTENT PLUGIN
class PeopleAppContentPlugin(AllinkManualEntriesMixin, AllinkBaseAppContentPlugin):
    """
    specify:

    TEMPLATES = (
        (AllinkBaseAppContentPlugin.GRID_STATIC, 'Grid (Static)'),
    )
    data_model = People

    manual_entries = SortedM2MModelField(
        People, blank=True,
        help_text=_('Select and arrange specific entries, or, leave blank to select all. (If '
                    'manual entries are selected, the category filtering is not active.)')
    )

    """

    TEMPLATES = (
        (AllinkBaseAppContentPlugin.GRID_STATIC, 'Grid (Static)'),
        (AllinkBaseAppContentPlugin.LIST, 'List'),
    )
    data_model = People

    manual_entries = SortedM2MModelField(
        '{}.{}'.format(data_model._meta.app_label, data_model._meta.model_name), blank=True,
        help_text=_('Select and arrange specific entries, or, leave blank to select all. (If '
                    'manual entries are selected the category filtering will be ignored.)')
    )


class PeopleImage(AllinkBaseImage):
    people = SortableForeignKey(People,  verbose_name=_(u'Images'), help_text=_(u'The first image will be used as preview image.'), blank=True, null=True)
