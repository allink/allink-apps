# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.forms import SplitArrayField
from cms.plugin_base import CMSPluginBase

from cms.plugin_pool import plugin_pool
from allink_apps.contact.models import ContactRequestPlugin


class ContactRequestFormPluginForm(forms.ModelForm):
    internal_email_adresses = SplitArrayField(forms.EmailField(required=False), size=3)

    class Meta:
        from allink_apps.contact.models import ContactRequestPlugin
        model = ContactRequestPlugin
        fields = ('send_internal_mail', 'internal_email_adresses', 'from_email_address', 'send_external_mail', 'thank_you_text')


@plugin_pool.register_plugin
class CMSAllinkContactRequestPlugin(CMSPluginBase):
    model = ContactRequestPlugin
    name = _('ContactRequest')
    module = _("allink")
    form = ContactRequestFormPluginForm

    def get_render_template(self, context, instance, placeholder):
        template = 'contact/content.html'
        return template
