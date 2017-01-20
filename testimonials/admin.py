# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from adminsortable.admin import SortableTabularInline
from allink_core.allink_base.admin import AllinkBaseAdmin

from .models import TestimonialImage, Testimonial, TestimonialAppContentPlugin


class TestimonialImageInline(SortableTabularInline):
    model = TestimonialImage
    extra = 1
    verbose_name = 'IMAGES'
    verbose_name_plural = ''

@admin.register(Testimonial)
class TestimonialAdmin(AllinkBaseAdmin):
    search_fields = ('firstname', 'lastname',)
    list_display = ('firstname', 'lastname', 'get_categories', 'active', 'created', 'modified')

    inlines = [TestimonialImageInline, ]

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'active',
                    ('firstname','lastname'),
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
        return super(TestimonialAdmin, self).formfield_for_dbfield(db_field, **kwargs)


@admin.register(TestimonialAppContentPlugin)
class TestimonialAppContentPluginAdmin(admin.ModelAdmin):
    pass