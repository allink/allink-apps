# -*- coding: utf-8 -*-
import datetime
from django.utils.translation import ugettext_lazy as _
from django.db import models
from adminsortable.fields import SortableForeignKey
from parler.models import TranslatableModel, TranslatedFields
from djangocms_text_ckeditor.fields import HTMLField
from phonenumber_field.modelfields import PhoneNumberField
from allink_core.allink_base.models import model_fields

from aldryn_translation_tools.models import (
    TranslatedAutoSlugifyMixin,
    TranslationHelperMixin,
)
from aldryn_common.admin_fields.sortedm2m import SortedM2MModelField

from allink_core.allink_base.models.mixins import AllinkManualEntriesMixin
from allink_core.allink_base.models.managers import AllinkBaseModelManager
from allink_core.allink_base.models import AllinkBaseModel, AllinkBaseImage, AllinkBaseAppContentPlugin, AllinkContactFieldsModel


class Locations(TranslationHelperMixin, TranslatedAutoSlugifyMixin, TranslatableModel, AllinkContactFieldsModel, AllinkBaseModel):
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
    street = model_fields.Street()
    zip_code = model_fields.ZipCode()
    place = model_fields.Place()

    lat = models.FloatField(
        _(u'Latitude'),
        blank=True,
        null=True
    )
    lng = models.FloatField(
        _(u'Longitude'),
        blank=True,
        null=True
    )

    mon = models.CharField(_(u'Monday morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm"', blank=True, max_length=100)
    tue = models.CharField(_(u'Tuesday morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm"', blank=True, max_length=100)
    wed = models.CharField(_(u'Wednesday morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm"', blank=True, max_length=100)
    thu = models.CharField(_(u'Thursday morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm"', blank=True, max_length=100)
    fri = models.CharField(_(u'Friday morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm"', blank=True, max_length=100)
    sat = models.CharField(_(u'Saturday morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm"', blank=True, max_length=100)
    sun = models.CharField(_(u'Sunday morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm"', blank=True, max_length=100)
    mon_afternoon = models.CharField(_(u'Monday morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', blank=True, max_length=100)
    tue_afternoon = models.CharField(_(u'Tuesday morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', blank=True, max_length=100)
    wed_afternoon = models.CharField(_(u'Wednesday morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', blank=True, max_length=100)
    thu_afternoon = models.CharField(_(u'Thursday morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', blank=True, max_length=100)
    fri_afternoon = models.CharField(_(u'Friday mo morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', blank=True, max_length=100)
    sat_afternoon = models.CharField(_(u'Saturday  morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', blank=True, max_length=100)
    sun_afternoon = models.CharField(_(u'Sunday mo morning or whole day'), help_text=u'Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', blank=True, max_length=100)

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

    def value_has_changed_for_fields(instance, fields):
        """
        Did any field values change since the last time they were saved?
        """
        if not instance.pk:  # if new
            return True
        old_values = instance.__class__._default_manager.filter(pk=instance.pk).values().get()
        for f in fields:
            if not getattr(instance, f) == old_values[f]:
                return True
        return False

    def geocode_location(self):
        """
        Update lat and lng fields based on address
        """
        from geopy import geocoders
        g = geocoders.GoogleV3()
        try:
            place, (lat, lng) = g.geocode((u'%s %s %s, Schweiz' % (self.street, self.zip_code, self.place)).encode("utf-8"))
        except Exception as e:
            return "%s: %s" % (self, e)
        else:
            self.lat = lat
            self.lng = lng
        return True

    def is_currently_open(self):
        opening_times = [
            (self.mon, self.mon_afternoon),
            (self.tue, self.tue_afternoon),
            (self.wed, self.wed_afternoon),
            (self.thu, self.thu_afternoon),
            (self.fri, self.fri_afternoon),
            (self.sat, self.sat_afternoon),
            (self.sun, self.sun_afternoon)
        ]
        return self.opening_info(opening_times[datetime.date.today().weekday()])
    is_currently_open.boolean = True
    is_currently_open.short_description = _(u'Now open_(u')

    def opening_info(self, times):
        """
        For the given times attr and the current time,
        is our store open?
        """
        morning = times[0]
        afternoon = times[1]

        try:
            current_time = datetime.datetime.today().time()
            morning_splited = morning.split('-')

            start_morning = morning_splited[0]
            end_morning = morning_splited[1]

            start_time = datetime.datetime.strptime(start_morning, '%H:%M').time()
            end_time = datetime.datetime.strptime(end_morning, '%H:%M').time()

            if start_time < current_time and end_time > current_time:
                return True

            elif afternoon:
                afternoon_splited = afternoon.split('-')

                start_afternoon = afternoon_splited[0]
                end_afternoon = afternoon_splited[1]

                start_time_afternoon = datetime.datetime.strptime(start_afternoon, '%H:%M').time()
                end_time_afternoon = datetime.datetime.strptime(end_afternoon, '%H:%M').time()

                if start_time_afternoon < current_time and end_time_afternoon > current_time:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False

    def has_opening_info(self):
        """
        Returns whether store has any filled in opening info
        If all fields are empty, returns False, else True
        """
        return reduce(
            lambda x, y: x or y,
            [
                self.mon,
                self.mon_afternoon,
                self.tue,
                self.tue_afternoon,
                self.wed,
                self.wed_afternoon,
                self.thu,
                self.thu_afternoon,
                self.fri,
                self.fri_afternoon,
                self.sat,
                self.sat_afternoon,
                self.sun,
                self.sun_afternoon
            ],
            False
        )

    def gmaps_link(self):
        """
        Returns google maps link with query of current store
        """
        return (u"https://www.google.ch/maps?q=Chicorée+Mode+AG+%(street)s+%(zip_code)s+%(place)s" % {
            'street': self.street,
            'zip_code': self.zip_code,
            'place': self.place
        }).replace(' ', '+')


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
