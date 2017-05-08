# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models

from cms.models.fields import PlaceholderField
from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin
from parler.models import TranslatableModel, TranslatedFields
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField

from aldryn_translation_tools.models import TranslationHelperMixin
from aldryn_common.admin_fields.sortedm2m import SortedM2MModelField

from allink_core.allink_base.models import AllinkManualEntriesMixin, AllinkBaseModelManager
from allink_core.allink_base.models import AllinkBaseModel, AllinkBaseImage, AllinkBaseAppContentPlugin
from allink_core.allink_base.models.mixins import AllinkTranslatedAutoSlugifyMixin


class Work(SortableMixin, TranslationHelperMixin, AllinkTranslatedAutoSlugifyMixin, TranslatableModel, AllinkBaseModel):

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
    sort_order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True
    )

    header_placeholder = PlaceholderField(u'work_header', related_name='%(app_label)s_%(class)s_header_placeholder')
    content_placeholder = PlaceholderField(u'work_content', related_name='%(app_label)s_%(class)s_content_placeholder')
    content_additional_placeholder = PlaceholderField(u'work_content_additional', related_name='%(app_label)s_%(class)s_content_additional_placeholder')

    objects = AllinkBaseModelManager()

    class Meta:
        app_label = 'work'
        ordering = ('sort_order',)
        verbose_name = _('Projekt/ Referenz')
        verbose_name_plural = _('Projekte/ Referenzen')


class Highlights(SortableMixin):
    text = models.CharField(max_length=80),
    work = SortableForeignKey(
        Work,
        verbose_name=_(u'Highlights'),
        blank=True,
        null=True
    )

    sort_order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True
    )

    def __str__(self):
        return str(self.text)

    class Meta:
        ordering = ('sort_order',)


# APP CONTENT PLUGIN
class WorkAppContentPlugin(AllinkManualEntriesMixin, AllinkBaseAppContentPlugin):

    data_model = Work

    manual_entries = SortedM2MModelField(
        '{}.{}'.format(data_model._meta.app_label, data_model._meta.model_name), blank=True,
        help_text=_('Select and arrange specific entries, or, leave blank to select all. (If '
                    'manual entries are selected the category filtering will be ignored.)')
    )


class WorkImage(AllinkBaseImage):
    work = SortableForeignKey(Work, verbose_name=_(u'Images'), help_text=_(u'The first image will be used as preview image.'), blank=True, null=True)
