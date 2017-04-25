# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from adminsortable.admin import SortableTabularInline

from allink_core.allink_base.admin import AllinkBaseAdmin
from allink_core.allink_base.admin.forms import AllinkBaseAdminForm
from allink_apps.people.models import PeopleImage, People


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
    search_fields = ('firstname', 'lastname',)
    list_display = ('firstname', 'lastname', 'get_categories', 'is_active', 'created', 'modified')

    exclude = ('images',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'is_active',
                    ('firstname', 'lastname'),
                    ('job_title', 'job_function'),
                    ('email', 'website'),
                    'company_name',
                    ('phone', 'mobile', 'fax'),
                    ('street', 'street_nr'),
                    'street_additional',
                    ('place', 'zip_code'),
                    'slug',
                ),
            }),
        )

        fieldsets += self.get_base_fieldsets()

        return fieldsets
