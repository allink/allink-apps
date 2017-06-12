# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

from cms.admin.placeholderadmin import PlaceholderAdminMixin
from adminsortable.admin import SortableTabularInline
from allink_core.allink_base.admin import AllinkBaseAdmin

from allink_apps.testimonials.models import TestimonialImage, Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(PlaceholderAdminMixin, AllinkBaseAdmin):
    search_fields = ('firstname', 'lastname',)
    # list_display = ('firstname', 'lastname', 'get_categories', 'is_active', 'created', 'modified')
    list_display = ('firstname', 'get_categories', 'is_active', 'created', 'modified')

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'is_active',
                    'firstname',
                    # ('firstname', 'lastname'),
                    # ('street', 'street_nr'),
                    # 'street_additional',
                    # ('place', 'zip_code'),
                    # 'lead',
                    # 'text',
                    'slug',
                    'created',
                    'preview_image',
                ),
            }),
        )

        fieldsets += self.get_base_fieldsets()

        return fieldsets

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'lead':
            kwargs['widget'] = forms.Textarea
        return super(TestimonialAdmin, self).formfield_for_dbfield(db_field, **kwargs)
