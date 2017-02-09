# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from import_export.admin import ImportExportMixin
from parler.admin import TranslatableAdmin
from aldryn_translation_tools.admin import AllTranslationsMixin

from allink_core.allink_mailchimp.config import MailChimpConfig

from .models import Members, MembersLog
from .resources import MembersResource
from .email import send_welcome_email
from .forms import MembersAdminForm


config = MailChimpConfig()


class MembersLogAdminInline(admin.TabularInline):
    model = MembersLog
    readonly_fields = ('description', 'created')
    extra = 0

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


def send_password_create_email(modeladmin, request, queryset):
    for member in queryset:
        send_welcome_email(request, member)
send_password_create_email.short_description = _(u'Send welcome email')


class MembersAdmin(ImportExportMixin, AllTranslationsMixin, TranslatableAdmin):
    resource_class = MembersResource

    list_display = ('member_nr', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email', 'language')
    inlines = [MembersLogAdminInline]
    readonly_fields = ('user', )
    actions = [send_password_create_email]
    form = MembersAdminForm

    def save_model(self, request, obj, form, change):
        super(MembersAdmin, self).save_model(request, obj, form, change)

        # update mailchimp list
        obj.put_to_mailchimp_list(form.initial.get('email'))

        if 'email' in form.changed_data:
            obj.log('email_changed_admin', u'Email-Address changed in Django admin.')

        if 'first_name' in form.changed_data:
            obj.log('first_name_changed_admin', u'Firstname changed in Django admin.')

        if 'last_name' in form.changed_data:
            obj.log('lastname_name_changed_admin', u'Lastname changed in Django admin.')


admin.site.register(Members, MembersAdmin)
