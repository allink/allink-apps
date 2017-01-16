# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from adminsortable.admin import SortableTabularInline
from allink_core.allink_base.admin import AllinkBaseAdmin

from .models import BrandsImage, Brands, BrandsAppContentPlugin


class BrandsImageInline(SortableTabularInline):
    model = BrandsImage
    extra = 1
    verbose_name = 'IMAGES'
    verbose_name_plural = ''

@admin.register(Brands)
class BrandsAdmin(AllinkBaseAdmin):
    search_fields = ('title',)
    list_display = ('title', 'get_categories', 'active', 'created', 'modified')

    inlines = [BrandsImageInline, ]

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'active',
                    'title',
                    'slug',
                    'lead',
                    'text',
                ),
            }),
        )

        fieldsets += self.get_base_fieldsets()

        return fieldsets

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'lead':
            kwargs['widget'] = forms.Textarea
        return super(BrandsAdmin, self).formfield_for_dbfield(db_field, **kwargs)


@admin.register(BrandsAppContentPlugin)
class BrandsAppContentPluginAdmin(admin.ModelAdmin):
    pass
