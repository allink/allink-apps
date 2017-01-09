# -*- coding: utf-8 -*-
from django.contrib import admin
from adminsortable.admin import SortableStackedInline
from django.utils.translation import ugettext_lazy as _
from allink_core.allink_base.admin import AllinkBaseAdmin

from .models import BlogImage, Blog, News, Events, BlogAppContentPlugin


class BlogImageInline(SortableStackedInline):
    model = BlogImage
    extra = 1
    verbose_name = 'IMAGES'
    verbose_name_plural = ''


@admin.register(Blog)
class BlogAdmin(AllinkBaseAdmin):
    inlines = [BlogImageInline, ]

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'title',
                    'slug',
                    'active',
                    'text',
                ),
            }),
        )

        fieldsets += (_('Published Form/ To'), {
            'classes': ('collapse',),
            'fields': (
                'start',
                'end',
            )
        }),

        if self.model.get_can_have_categories():
            fieldsets += (_('Categories'), {
                'fields': (
                    'categories',
                )
            }),

        return fieldsets

@admin.register(News)
class NewsAdmin(AllinkBaseAdmin):
    inlines = [BlogImageInline, ]

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'title',
                    'slug',
                    'active',
                    'text',
                ),
            }),
        )

        fieldsets += (_('Published Form/ To'), {
            'classes': ('collapse',),
            'fields': (
                'start',
                'end',
            )
        }),

        if self.model.get_can_have_categories():
            fieldsets += (_('Categories'), {
                'fields': (
                    'categories',
                )
            }),

        return fieldsets


@admin.register(Events)
class EventsAdmin(AllinkBaseAdmin):
    inlines = [BlogImageInline, ]

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'title',
                    'slug',
                    'active',
                    'lead',
                    'text',
                    ('event_date', 'costs', )
                ),
            }),
        )

        fieldsets += (_('Published Form/ To'), {
            'classes': ('collapse',),
            'fields': (
                'start',
                'end',
            )
        }),

        if self.model.get_can_have_categories():
            fieldsets += (_('Categories'), {
                'fields': (
                    'categories',
                )
            }),

        return fieldsets


@admin.register(BlogAppContentPlugin)
class BlogAppContentPluginAdmin(admin.ModelAdmin):
    pass
