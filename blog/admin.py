# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from adminsortable.admin import SortableTabularInline
from allink_core.allink_base.admin import AllinkBaseAdmin
from allink_core.allink_base.admin.forms import AllinkBaseAdminForm
from allink_core.allink_categories.models import AllinkCategory
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from allink_apps.blog.models import BlogImage, Blog, News, Events, EventsRegistration


class BlogContentAdminForm(AllinkBaseAdminForm):

    def __init__(self, *args, **kwargs):
        super(BlogContentAdminForm, self).__init__(*args, **kwargs)
        self.fields['categories'].initial = AllinkCategory.objects.not_root().filter(translations__name__iexact=self._meta.model._meta.model_name)


class BlogImageInline(SortableTabularInline):
    model = BlogImage
    extra = 1
    verbose_name = 'IMAGES'
    verbose_name_plural = ''


@admin.register(News)
class NewsAdmin(PlaceholderAdminMixin, AllinkBaseAdmin):
    form = BlogContentAdminForm
    inlines = [BlogImageInline, ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'lead':
            kwargs['widget'] = forms.Textarea
        return super(NewsAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'active',
                    'title',
                    'slug',
                    'created',
                    'lead',
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
class EventsAdmin(PlaceholderAdminMixin, AllinkBaseAdmin):
    list_display = ('title', 'get_categories', 'event_date', 'active', )
    inlines = [BlogImageInline, ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'lead':
            kwargs['widget'] = forms.Textarea
        return super(EventsAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'active',
                    'title',
                    'slug',
                    'created',
                    'lead',
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

@admin.register(EventsRegistration)
class EventsRegistrationAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(PlaceholderAdminMixin, AllinkBaseAdmin):
    inlines = [BlogImageInline, ]
