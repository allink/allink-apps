# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms

from cms.admin.placeholderadmin import PlaceholderAdminMixin
from adminsortable.admin import SortableTabularInline
from allink_core.allink_base.admin import AllinkBaseAdmin

from .models import WorkImage, Work


class WorkImageInline(SortableTabularInline):
    model = WorkImage
    extra = 1
    verbose_name = 'IMAGES'
    verbose_name_plural = ''

@admin.register(Work)
class WorkAdmin(PlaceholderAdminMixin, AllinkBaseAdmin):
    inlines = [WorkImageInline, ]
    # list_filter = ('active', 'categories',)

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
        return super(WorkAdmin, self).formfield_for_dbfield(db_field, **kwargs)