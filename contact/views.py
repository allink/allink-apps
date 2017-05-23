# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from allink_core.allink_base.views import AllinkBaseCreateView
from allink_core.allink_mandrill.config import MandrillConfig

from allink_apps.contact.models import ContactRequest, ContactRequestPlugin
from allink_apps.contact.forms import ContactRequestForm
from allink_apps.contact.email import send_request_confirmation_email, send_request_email

config = MandrillConfig()


class ContactRequestView(AllinkBaseCreateView):
    model = ContactRequest
    form_class = ContactRequestForm
    template_name = 'contact/forms/request.html'
    plugin = None

    def dispatch(self, *args, **kwargs):
        plugin_id = self.kwargs.pop('plugin_id', None)
        if plugin_id:
            self.plugin = ContactRequestPlugin.objects.get(id=plugin_id)
        return super(ContactRequestView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        response = super(ContactRequestView, self).form_valid(form)
        self.send_mail()
        return response

    def send_mail(self):
        if not self.plugin or self.plugin.send_internal_mail:
            send_request_email(self.get_form(), self.plugin)
        if not self.plugin or self.plugin.send_external_mail:
            send_request_confirmation_email(self.get_form(), self.plugin)
