# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from adminsortable.fields import SortableForeignKey
from parler.models import TranslatableModel, TranslatedFields
from djangocms_text_ckeditor.fields import HTMLField

from aldryn_translation_tools.models import (
    TranslatedAutoSlugifyMixin,
    TranslationHelperMixin,
)
from aldryn_common.admin_fields.sortedm2m import SortedM2MModelField

from allink_core.allink_base.models.mixins import AllinkManualEntriesMixin
from allink_core.allink_base.models import AllinkBaseModelManager
from allink_core.allink_base.models import AllinkBaseModel, AllinkBaseImage, AllinkBaseAppContentPlugin


class Work(TranslationHelperMixin, TranslatedAutoSlugifyMixin, TranslatableModel, AllinkBaseModel):
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
            help_text=_(u'Used as a teaser. Not displayed in detail view.'),
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

    objects = AllinkBaseModelManager()

    class Meta:
        app_label = 'work'
        verbose_name = _('Geschichte')
        verbose_name_plural = _('Geschichten')

    @property
    def preview_image(self):
        if self.workimage_set.count() > 0:
            return self.workimage_set.first().image

    @property
    def images(self):
        return self.workimage_set.all()


# APP CONTENT PLUGIN
class WorkAppContentPlugin(AllinkManualEntriesMixin, AllinkBaseAppContentPlugin):
    """
    """
    data_model = Work

    manual_entries = SortedM2MModelField(
        '{}.{}'.format(data_model._meta.app_label, data_model._meta.model_name), blank=True,
        help_text=_('Select and arrange specific entries, or, leave blank to select all. (If '
                    'manual entries are selected the category filtering will be ignored.)')
    )


class WorkImage(AllinkBaseImage):
    work = SortableForeignKey(Work,  verbose_name=_(u'Images'), help_text=_(u'The first image will be used as preview image.'), blank=True, null=True)
