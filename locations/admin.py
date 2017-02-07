# -*- coding: utf-8 -*-
from django.contrib import admin
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
                ),
            }),
        )

        fieldsets += self.get_base_fieldsets()

        return fieldsets

#
# @admin.register(LocationsAppContentPlugin)
# class LocationsAppContentPluginAdmin(admin.ModelAdmin):
#     pass
