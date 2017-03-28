# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from adminsortable.admin import SortableTabularInline

from allink_core.allink_base.admin import AllinkBaseAdmin
from allink_core.allink_base.admin.forms import AllinkBaseAdminForm
from .models import PeopleImage, People

class PeopleImageInline(SortableTabularInline):
    model = PeopleImage
    extra = 1
    max_num = 1
    verbose_name = None
    verbose_name_plural = _(u'Preview Image')


@admin.register(People)
class PeopleAdmin(PlaceholderAdminMixin, AllinkBaseAdmin):
    inlines = [PeopleImageInline, ]

    form = AllinkBaseAdminForm
    search_fields = ('translations__firstname', 'translations__lastname',)
    list_display = ('firstname', 'lastname', 'get_categories', 'active', 'created', 'modified')

    exclude = ('images',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'active',
                    ('firstname', 'lastname'),
                    ('job_title', 'job_function'),
                    ('email', 'website'),
                    'company_name',
                    ('phone', 'mobile', 'fax'),
                    ('street', 'street_nr'),
                    ('place', 'zip_code'),
                    'slug',
                ),
            }),
        )

        fieldsets += self.get_base_fieldsets()

        return fieldsets