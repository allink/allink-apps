# -*- coding: utf-8 -*-
from django.contrib import admin
from adminsortable.admin import SortableStackedInline
from django.utils.translation import ugettext_lazy as _
from allink_core.allink_base.admin import AllinkBaseAdmin

from .models import LocationsImage, Locations, LocationsAppContentPlugin


class LocationsImageInline(SortableStackedInline):
    model = LocationsImage
    extra = 1
    verbose_name = 'IMAGES'
    verbose_name_plural = ''

@admin.register(Locations)
class LocationsAdmin(AllinkBaseAdmin):
    inlines = [LocationsImageInline, ]

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'title',
                    'slug',
                    'active',
                    'text',
                    ('zip', 'city',),
                    'street',
                    ('phone', 'mobile',),
                    ('email', 'fax',),
                    ('lat', 'lng',),
                ),
            }),
        )

        if self.model.get_can_have_categories():
            fieldsets += (_('Categories'), {
                'fields': (
                    'categories',
                )
            }),

        return fieldsets


@admin.register(LocationsAppContentPlugin)
class LocationsAppContentPluginAdmin(admin.ModelAdmin):
    pass
