# -*- coding: utf-8 -*-
from django.contrib import admin
from adminsortable.admin import SortableStackedInline
from django.utils.translation import ugettext_lazy as _
from allink_core.allink_base.admin import AllinkBaseAdmin

from .models import WorkImage, Work, WorkAppContentPlugin


class WorkImageInline(SortableStackedInline):
    model = WorkImage
    extra = 1
    verbose_name = 'IMAGES'
    verbose_name_plural = ''

@admin.register(Work)
class WorkAdmin(AllinkBaseAdmin):
    inlines = [WorkImageInline, ]

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'title',
                    'slug',
                    'active',
                    'lead',
                    'text',
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


@admin.register(WorkAppContentPlugin)
class WorkAppContentPluginAdmin(admin.ModelAdmin):
    pass
