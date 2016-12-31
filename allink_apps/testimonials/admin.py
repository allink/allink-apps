# -*- coding: utf-8 -*-
from django.contrib import admin
from adminsortable.admin import SortableStackedInline
from django.utils.translation import ugettext_lazy as _
from allink_core.allink_base.admin import AllinkBaseAdmin

from .models import TestimonialImage, Testimonial, TestimonialAppContentPlugin


class TestimonialImageInline(SortableStackedInline):
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
                    'firstname',
                    'lastname',
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


@admin.register(TestimonialAppContentPlugin)
class TestimonialAppContentPluginAdmin(admin.ModelAdmin):
    pass
