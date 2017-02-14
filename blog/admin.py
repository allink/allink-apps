# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from adminsortable.admin import SortableTabularInline
from allink_core.allink_base.admin import AllinkBaseAdmin

from .models import BlogImage, Blog, News, Events, EventsRegistration

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
                    'created',
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
                    'created',
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
    list_display = ('title', 'event_date', 'active', )

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'active',
                    'title',
                    'slug',
                    'created',
                    'lead',
                    'text',
                    'location',
                    'form_enabled',
                    ('event_date', 'event_time', 'costs', )
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


class EventsRegistrationAdmin(admin.ModelAdmin):
    pass
