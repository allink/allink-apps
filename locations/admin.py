# -*- coding: utf-8 -*-
from django.contrib import admin, messages
from adminsortable.admin import SortableTabularInline
from django.utils.translation import ugettext_lazy as _
from allink_core.allink_base.admin import AllinkBaseAdmin

from .models import LocationsImage, Locations, LocationsAppContentPlugin


class LocationsImageInline(SortableTabularInline):
    model = LocationsImage
    extra = 1
    verbose_name = 'IMAGES'
    verbose_name_plural = ''

@admin.register(Locations)
class LocationsAdmin(AllinkBaseAdmin):
    inlines = [LocationsImageInline, ]
    exclude = ('lead', )
    readonly_fields = ('is_currently_open', )

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'active',
                    'title',
                    'slug',
                    'text',
                    ('zip_code', 'place',),
                    'street',
                    ('phone', 'mobile',),
                    ('email', 'fax',),
                    ('lat', 'lng',),
                    'is_currently_open',
                ),
            }),
            (_(u'Opening hours'), {
                'fields': ('is_currently_open', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'),
                'description': _(u'Format: "9:00-12:00  13:00-20:00"')
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
