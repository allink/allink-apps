# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models

from cms.models.fields import PlaceholderField
from adminsortable.fields import SortableForeignKey
from parler.models import TranslatableModel, TranslatedFields
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField

from aldryn_translation_tools.models import TranslationHelperMixin
from aldryn_common.admin_fields.sortedm2m import SortedM2MModelField

from allink_core.allink_base.models.mixins import AllinkManualEntriesMixin
from allink_core.allink_base.models import AllinkBaseModel, AllinkBaseImage, AllinkBaseAppContentPlugin
from allink_core.allink_base.models import AllinkAddressFieldsModel, AllinkTranslatedAutoSlugifyMixin

from allink_apps.testimonials.managers import AllinkTestimonialManager


class Testimonial(TranslationHelperMixin, AllinkTranslatedAutoSlugifyMixin, TranslatableModel, AllinkAddressFieldsModel, AllinkBaseModel):
    """
    Translations
     feel free to add app specific fields)
     to override slug generation:
     slug_source_field_name = 'title'

    """
    slug_source_field_name = 'full_name'

    title = models.CharField(
        _(u'Name'),
        max_length=255,
        default=''
    )

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
        # to be removed in release 0.0.9, or when all old projects are up to date
        old_firstname=models.CharField(
            _(u'Firstname'),
            max_length=255,
            default=''
        ),
        # to be removed in release 0.0.9, or when all old projects are up to date
        old_lastname=models.CharField(
            _(u'Lastname'),
            max_length=255,
            default=''
        ),
        slug=models.SlugField(
            _(u'Slug'),
            max_length=255,
            default='',
            blank=True,
            help_text=_(u'Leave blank to auto-generate a unique slug.')
        ),
        lead=HTMLField(
            _(u'Lead text'),
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

    header_placeholder = PlaceholderField(u'testimonial_header', related_name='%(app_label)s_%(class)s_header_placeholder')
    content_placeholder = PlaceholderField(u'testimonial_content', related_name='%(app_label)s_%(class)s_content_placeholder')

    objects = AllinkTestimonialManager()

    class Meta:
        app_label = 'testimonials'
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

    @property
    def full_name(self):
        return u'{} {}'.format(self.firstname, self.lastname)

    @property
    def title(self):
        return u'{} {}'.format(self.firstname, self.lastname)


# APP CONTENT PLUGIN
class TestimonialAppContentPlugin(AllinkManualEntriesMixin, AllinkBaseAppContentPlugin):
    """
    There should be no need to extend this Model.
    All the configuration can be done with the funtionallity of Basemodel "AllinkAppContent".
    """
    TEMPLATES = (
        (AllinkBaseAppContentPlugin.GRID_STATIC, 'Grid (Static)'),
        (AllinkBaseAppContentPlugin.GRID_DYNAMIC, 'Grid (Dynamic)'),
        (AllinkBaseAppContentPlugin.SLIDER, 'Slider'),
    )
    data_model = Testimonial

    manual_entries = SortedM2MModelField(
        '{}.{}'.format(data_model._meta.app_label, data_model._meta.model_name), blank=True,
        help_text=_('Select and arrange specific entries, or, leave blank to select all. (If '
                    'manual entries are selected the category filtering will be ignored.)')
    )


class TestimonialImage(AllinkBaseImage):
    testimonial = SortableForeignKey(Testimonial, verbose_name=_(u'Images'), help_text=_(u'The first image will be used as preview image.'), blank=True, null=True)
