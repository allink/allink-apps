# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms

from parler.admin import TranslatableTabularInline
from adminsortable.admin import SortableTabularInline
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from allink_core.allink_base.admin import AllinkBaseAdminSortable

from allink_apps.work.models import Work


@admin.register(Work)
class WorkAdmin(PlaceholderAdminMixin, AllinkBaseAdminSortable):
    list_filter = ('is_active', 'categories',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'is_active',
                    'title',
                    'slug',
                    'lead',
                    'preview_image',
                ),
            }),
        )

        fieldsets += self.get_base_fieldsets()

        return fieldsets

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'lead':
            kwargs['widget'] = forms.Textarea
        return super(WorkAdmin, self).formfield_for_dbfield(db_field, **kwargs)
