# -*- coding: utf-8 -*-
import phonenumbers
from django.utils.translation import ugettext_lazy as _
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from adminsortable.fields import SortableForeignKey
from parler.models import TranslatableModel, TranslatedFields
from phonenumber_field.modelfields import PhoneNumberField
from aldryn_translation_tools.models import (
    TranslatedAutoSlugifyMixin,
    TranslationHelperMixin,
)
from aldryn_common.admin_fields.sortedm2m import SortedM2MModelField

from allink_core.allink_base.models.choices import GENDER_CHOICES
from allink_core.allink_base.models import AllinkBaseModelManager
from allink_core.allink_base.models.mixins import AllinkManualEntriesMixin
from allink_core.allink_base.models import AllinkBaseModel, AllinkBaseImage, AllinkBaseAppContentPlugin

from .managers import AllinkPeopleManager


class People(TranslationHelperMixin, TranslatedAutoSlugifyMixin, TranslatableModel, AllinkBaseModel):
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

    gender = models.IntegerField(
        _(u'Gender'),
        choices=GENDER_CHOICES,
        null=True
    )
    phone = PhoneNumberField(
        _(u'Phone'),
        blank=True,
        null=True
    )
    mobile = PhoneNumberField(
        _(u'Mobile'),
        blank=True,
        null=True
    )
    fax = PhoneNumberField(
        _(u'Fax'),
        blank=True,
        null=True
    )
    email = models.EmailField(
        _(u'Email'),
        blank=True,
        default=''
    )
    website = models.URLField(
        _(u'Website'),
        blank=True,
        null=True
    )

    objects = AllinkPeopleManager()

    class Meta:
        app_label = 'people'
        verbose_name = _('Person')
        verbose_name_plural = _('People')

    @property
    def full_name(self):
        return u'{} {}'.format(self.lastname, self.firstname)

    @property
    def formatted_phone(self):
        x = phonenumbers.parse(str(self.phone), None)
        return str(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL))

    @property
    def preview_image(self):
        if self.peopleimage_set.count() > 0:
            return self.peopleimage_set.first().image

    @property
    def title(self):
        return u'{} {}'.format(self.lastname, self.firstname)


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
    )
    data_model = People

    manual_entries = SortedM2MModelField(
        '{}.{}'.format(data_model._meta.app_label, data_model._meta.model_name), blank=True,
        help_text=_('Select and arrange specific entries, or, leave blank to select all. (If '
                    'manual entries are selected the category filtering will be ignored.)')
    )


class PeopleImage(AllinkBaseImage):
    people = SortableForeignKey(People,  verbose_name=_(u'Images'), help_text=_(u'The first image will be used as preview image.'), blank=True, null=True)
