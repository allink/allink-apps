# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from adminsortable.admin import SortableTabularInline
from django.utils.translation import ugettext_lazy as _
from allink_core.allink_base.admin import AllinkBaseAdmin

from .models import BlogImage, Blog, News, Events, Teachers, Courses, BlogAppContentPlugin

class BlogImageInline(SortableTabularInline):
    model = BlogImage
    extra = 1
    verbose_name = 'IMAGES'
    verbose_name_plural = ''


@admin.register(Blog)
class BlogAdmin(AllinkBaseAdmin):
    inlines = [BlogImageInline, ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'lead':
            kwargs['widget'] = forms.Textarea
        return super(BlogAdmin, self).formfield_for_dbfield(db_field, **kwargs)

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

        fieldsets += (_('Published From/To'), {
            'classes': ('collapse',),
            'fields': (
                'start',
                'end',
            )
        }),

        fieldsets += self.get_base_fieldsets()

        return fieldsets

@admin.register(News)
class NewsAdmin(BlogAdmin):

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

        fieldsets += (_('Published From/To'), {
            'classes': ('collapse',),
            'fields': (
                'start',
                'end',
            )
        }),

        fieldsets += self.get_base_fieldsets()

        return fieldsets


@admin.register(Events)
class EventsAdmin(BlogAdmin):

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'active',
                    'title',
                    'slug',
                    'lead',
                    'text',
                    ('event_date', 'costs', )
                ),
            }),
        )

        fieldsets += (_('Published From/To'), {
            'classes': ('collapse',),
            'fields': (
                'start',
                'end',
            )
        }),

        fieldsets += self.get_base_fieldsets()

        return fieldsets


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    pass


class TeachersInline(SortableTabularInline):
    model = Teachers
    extra = 1
    verbose_name = None
    verbose_name_plural = ''


@admin.register(Courses)
class CoursesAdmin(BlogAdmin):
    inlines = [BlogImageInline, TeachersInline, ]

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'title',
                    'slug',
                    'active',
                    'lead',
                    'text',
                    'location',
                    ('duration', 'costs', )
                ),
            }),
        )

        fieldsets += (_('Published From/To'), {
            'classes': ('collapse',),
            'fields': (
                'start',
                'end',
            )
        }),

        fieldsets += self.get_base_fieldsets()

        return fieldsets


@admin.register(BlogAppContentPlugin)
class BlogAppContentPluginAdmin(admin.ModelAdmin):
    pass
