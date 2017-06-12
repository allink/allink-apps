# -*- coding: utf-8 -*-
from django.contrib import admin, messages
from django.utils.translation import ugettext_lazy as _

from cms.admin.placeholderadmin import PlaceholderAdminMixin
from adminsortable.admin import SortableTabularInline
from allink_core.allink_base.admin import AllinkBaseAdmin

from allink_apps.locations.models import LocationsImage, Locations

@admin.register(Locations)
class LocationsAdmin(PlaceholderAdminMixin, AllinkBaseAdmin):
    exclude = ('lead', )
    readonly_fields = ('is_currently_open', )

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'is_active',
                    'title',
                    'slug',
                    'subtitle',
                    ('lat', 'lng',),
                    ('street', 'street_nr',),
                    ('zip_code', 'place',),
                    'street_additional',
                    ('phone', 'mobile',),
                    ('email', 'fax',),
                    'website',
                    'map_link',
                    'preview_image',
                    'opening_hours_display',
                ),
            }),
            (_(u'Opening hours (Detailed)'), {
                'classes': ('collapse',),
                'fields': (
                    'is_currently_open',
                    'mon',
                    'mon_afternoon',
                    'tue',
                    'tue_afternoon',
                    'wed',
                    'wed_afternoon',
                    'thu',
                    'thu_afternoon',
                    'fri',
                    'fri_afternoon',
                    'sat',
                    'sat_afternoon',
                    'sun',
                    'sun_afternoon'),
                    'description': _(u'Format: "9:00-12:00  13:00-20:00"'
                )
            }),
        )

        fieldsets += self.get_base_fieldsets()

        return fieldsets

    def save_model(self, request, obj, form, change):
        if obj.value_has_changed_for_fields(["place", "zip_code", "street"]):
            msg = obj.geocode_location()
            if not msg:
                messages.warning(request, msg)
        super(self.__class__, self).save_model(request, obj, form, change)
