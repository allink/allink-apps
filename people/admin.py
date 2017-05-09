# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from allink_core.allink_base.admin import AllinkBaseAdmin, AllinkBaseAdminSortable
from allink_core.allink_base.admin.forms import AllinkBaseAdminForm
from allink_apps.people.models import People


@admin.register(People)
class PeopleAdmin(PlaceholderAdminMixin, AllinkBaseAdmin):

    form = AllinkBaseAdminForm
    search_fields = ('firstname', 'lastname',)
    list_display = ('firstname', 'lastname', 'get_categories', 'is_active', 'created', 'modified')

    exclude = ('images',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'is_active',
                    ('firstname', 'lastname'),
                    # ('job_title', 'job_function'),
                    ('email'),
                    # ('email', 'website'),
                    # 'company_name',
                    ('phone', 'mobile', 'fax'),
                    # ('street', 'street_nr'),
                    # 'street_additional',
                    # ('place', 'zip_code'),
                    'slug',
                    'preview_image',
                ),
            }),
        )

        fieldsets += self.get_base_fieldsets()

        return fieldsets
