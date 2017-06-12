# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from cms.admin.placeholderadmin import PlaceholderAdminMixin


from allink_core.allink_base.admin import AllinkBaseAdmin
from allink_core.allink_base.admin.forms import AllinkBaseAdminForm
from allink_core.allink_categories.models import AllinkCategory

from allink_core.allink_base.utils import get_additional_choices
from allink_apps.blog.models import Blog, News, Events, EventsRegistration


class BlogContentAdminForm(AllinkBaseAdminForm):

    def __init__(self, *args, **kwargs):
        super(BlogContentAdminForm, self).__init__(*args, **kwargs)
        self.fields['categories'].initial = AllinkCategory.objects.not_root().filter(translations__name__iexact=self._meta.model._meta.model_name)

        if get_additional_choices('ADDITIONAL_BLOG_DETAIL_TEMPLATES'):
            self.fields['template'] = forms.CharField(
                label=_(u'Template'),
                widget=forms.Select(choices=get_additional_choices('ADDITIONAL_BLOG_DETAIL_TEMPLATES', blank=True)),
                required=False,
            )
        else:
            self.fields['template'] = forms.CharField(widget=forms.HiddenInput(),)


@admin.register(News)
class NewsAdmin(PlaceholderAdminMixin, AllinkBaseAdmin):
    form = BlogContentAdminForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'lead':
            kwargs['widget'] = forms.Textarea
        return super(NewsAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'is_active',
                    'title',
                    'slug',
                    'created',
                    'template',
                    'preview_image',
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
    form = BlogContentAdminForm
    list_display = ('title', 'get_categories', 'event_date', 'is_active', )

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'lead':
            kwargs['widget'] = forms.Textarea
        return super(EventsAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'is_active',
                    'title',
                    'slug',
                    'template',
                    'preview_image',
                    ('event_date', 'event_time', 'costs', ),
                    'lead',
                    'location',
                    'form_enabled',
                    'created',
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
    list_display = ('__str__', 'email', 'created', 'event', 'message',)
    list_filter = ('event', )


@admin.register(Blog)
class BlogAdmin(PlaceholderAdminMixin, AllinkBaseAdmin):
    pass
