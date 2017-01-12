# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey
from parler.models import TranslatableModel, TranslatedFields
from djangocms_text_ckeditor.fields import HTMLField
from model_utils.models import TimeFramedModel

from aldryn_translation_tools.models import (
    TranslatedAutoSlugifyMixin,
    TranslationHelperMixin,
)
from aldryn_common.admin_fields.sortedm2m import SortedM2MModelField

from allink_core.allink_base.models.mixins import AllinkManualEntriesMixin
from allink_core.allink_base.models import AllinkBaseModelManager
from allink_core.allink_base.models import AllinkBaseModel, AllinkBaseImage, AllinkBaseAppContentPlugin
from allink_apps.people.models import People
from allink_apps.locations.models import Locations


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

# Events
class Events(Blog):

    translations_events = TranslatedFields(
        costs=models.CharField(
            max_length=255,
            help_text=_(u'Costs'),
            blank=True,
            null=True,
        )
    )

    event_date = models.DateField(
        _(u'Event Date'),
        blank=True,
        null=True,
    )

    event_time = models.CharField(
        max_length=255,
        help_text=_(u'Event Time'),
        blank=True,
        null=True,
    )

    # location = models.ForeignKey(Location)

    objects = AllinkBaseModelManager()

    class Meta:
        app_label = 'blog'
        verbose_name = _('Event')
        verbose_name_plural = _('Events')


# Courses/ Workshops
class Courses(Blog):

    translations_events = TranslatedFields(
        costs=models.CharField(
            max_length=255,
            help_text=_(u'Costs'),
            blank=True,
            null=True,
        )
    )

    duration = models.CharField(
        max_length=255,
        help_text=_(u'Duration'),
        blank=True,
        null=True,
    )

    location = models.ForeignKey(Locations, blank=True, null=True)

    objects = AllinkBaseModelManager()

    class Meta:
        app_label = 'blog'
        verbose_name = _('Courses/ Workshops')
        verbose_name_plural = _('Courses/ Workshops')



@python_2_unicode_compatible
class Teachers(SortableMixin):

    sort_order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True
    )
    internal = models.ForeignKey(
        People,
        verbose_name=_(u'Intern teacher'),
        blank=True,
        null=True
    )
    external = models.CharField(
        verbose_name=_(u'External teacher'),
        max_length=255,
        help_text=_(u'Intern teacher will override this field.'),
        blank=True,
        null=True
    )
    website = models.URLField(
        verbose_name=_(u'Link'),
        help_text=_(u'Only used when extern teacher is filled.'),
        blank=True,
        null=True
    )
    courses = SortableForeignKey(Courses, blank=True, null=True)

    class Meta:
        ordering = ('sort_order',)

    def __str__(self):
        if self.internal:
            return unicode(self.internal)
        elif self.external:
            return unicode(self.external)
        else:
            return _(u'Teacher')


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


class BlogImage(AllinkBaseImage):
    blog = SortableForeignKey(Blog,  verbose_name=_(u'Images'), help_text=_(u'The first image will be used as preview image.'), blank=True, null=True)
