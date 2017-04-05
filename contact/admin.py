# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from allink_apps.contact.models import ContactRequest


class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'created', 'modified', 'nicer_contact_type', 'date', 'time', 'message',)
    list_filter = ('contact_type', 'modified', )

    def nicer_contact_type(self, obj):
        return '%s (%s)'.format(obj.get_contact_type_display(), obj.contact_details)

    nicer_contact_type.short_description = _(u'Contact via')


admin.site.register(ContactRequest, ContactRequestAdmin)
