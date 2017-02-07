# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from adminsortable.fields import SortableForeignKey
from parler.models import TranslatableModel, TranslatedFields
from djangocms_text_ckeditor.fields import HTMLField
from phonenumber_field.modelfields import PhoneNumberField

from aldryn_translation_tools.models import (
    TranslatedAutoSlugifyMixin,
    TranslationHelperMixin,
)
from aldryn_common.admin_fields.sortedm2m import SortedM2MModelField

from allink_core.allink_base.models.mixins import AllinkManualEntriesMixin
from allink_core.allink_base.models.managers import AllinkBaseModelManager
from allink_core.allink_base.models import AllinkBaseModel, AllinkBaseImage, AllinkBaseAppContentPlugin, AllinkAddressBasicFieldsModel, AllinkContactFieldsModel


class Locations(TranslationHelperMixin, TranslatedAutoSlugifyMixin, TranslatableModel, AllinkAddressBasicFieldsModel, AllinkContactFieldsModel, AllinkBaseModel):
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

    lat = models.FloatField(
        _(u'Latitude'),
    )
    lng = models.FloatField(
        _(u'Longitude'),
    )

    # TODO:
    #  page = LINK to CMS Page (or Link to detail view from location app!)

    objects = AllinkBaseModelManager()

    class Meta:
        app_label = 'locations'
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    @property
    def preview_image(self):
        if self.locationsimage_set.count() > 0:
            return self.locationsimage_set.first().image

    @property
    def images(self):
        return self.locationsimage_set.all()


# APP CONTENT PLUGIN
class LocationsAppContentPlugin(AllinkManualEntriesMixin, AllinkBaseAppContentPlugin):
    """
    """
    # TEMPLATES = AllinkBaseAppContentPlugin.TEMPLATES \
    #             + ('map', 'Map')

    TEMPLATES = (
        # (AllinkBaseAppContentPlugin.GRID_STATIC, 'Grid (Static)'),
        # (AllinkBaseAppContentPlugin.GRID_DYNAMIC, 'Grid (Dynamic)'),
        ('map', 'Map'),
    )

    ZOOM_LEVEL_CHOICES = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
        (18, 18),
    )

    data_model = Locations

    manual_entries = SortedM2MModelField(
        '{}.{}'.format(data_model._meta.app_label, data_model._meta.model_name),
        blank=True,
        help_text=_('Select and arrange specific entries, or, leave blank to select all. (If '
                    'manual entries are selected the category filtering will be ignored.)')
    )

    zoom_level = models.IntegerField(
        _(u'Zoom Level'),
        help_text=_(u'The higher the number, the more we zoom in.'),
        choices=ZOOM_LEVEL_CHOICES,
        default=14
    )

class LocationsImage(AllinkBaseImage):
    location = SortableForeignKey(
        Locations,
        verbose_name=_(u'Images'),
        help_text=_(u'The first image will be used as preview image.'),
        blank=True,
        null=True
    )
