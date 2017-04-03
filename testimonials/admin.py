# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

from cms.admin.placeholderadmin import PlaceholderAdminMixin
from adminsortable.admin import SortableTabularInline
from allink_core.allink_base.admin import AllinkBaseAdmin

from .models import TestimonialImage, Testimonial, TestimonialAppContentPlugin


class TestimonialImageInline(SortableTabularInline):
    model = TestimonialImage
    extra = 0
    max_num = 1
    verbose_name = ''
    verbose_name_plural = _(u'Preview Image')

@admin.register(Testimonial)
class TestimonialAdmin(PlaceholderAdminMixin, AllinkBaseAdmin):
    search_fields = ('translations__firstname', 'translations__lastname',)
    list_display = ('firstname', 'lastname', 'get_categories', 'active', 'created', 'modified')

    inlines = [TestimonialImageInline, ]

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'active',
                    ('firstname','lastname'),
                    ('street', 'street_nr'),
                    ('place', 'zip_code'),
                    'lead',
                    'text',
                    'slug',
                    'created',
                ),
            }),
        )

        fieldsets += self.get_base_fieldsets()

        return fieldsets

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'lead':
            kwargs['widget'] = forms.Textarea
        return super(TestimonialAdmin, self).formfield_for_dbfield(db_field, **kwargs)
