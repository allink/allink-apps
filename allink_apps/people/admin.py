# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from adminsortable.admin import SortableTabularInline
from allink_core.allink_base.admin import AllinkBaseAdmin
from allink_core.allink_base.admin.forms import AllinkBaseAdminForm
from .models import PeopleImage, People, PeopleAppContentPlugin

class PeopleImageInline(SortableTabularInline):
    model = PeopleImage
    extra = 1
    verbose_name = None
    verbose_name_plural = ''


@admin.register(People)
class PeopleAdmin(AllinkBaseAdmin):
    inlines = [PeopleImageInline, ]

    form = AllinkBaseAdminForm
    search_fields = ('firstname', 'lastname',)
    list_display = ('firstname', 'lastname', 'get_categories', 'active', 'created', 'modified')
    list_filter = ('active',)

    exclude = ('images',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (None, {
                'fields': (
                    'active',
                    ('firstname', 'lastname', 'gender'),
                    ('job_title', 'job_function'),
                    ('email', 'website'),
                    ('company_name', 'place'),
                    ('phone', 'mobile', 'fax'),
                    'text',
                    'slug',
                ),
            }),
        )

        fieldsets += self.get_base_fieldsets()

        return fieldsets


@admin.register(PeopleAppContentPlugin)
class PeopleAppContentPluginAdmin(admin.ModelAdmin):
    pass
