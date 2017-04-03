# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from allink_core.allink_base.views import AllinkBaseCreateView
from allink_core.allink_mandrill.config import MandrillConfig

from .models import ContactRequest
from .forms import ContactRequestForm
from .email import send_request_confirmation_email, send_request_email

config = MandrillConfig()

class ContactRequestView(AllinkBaseCreateView):
    model = ContactRequest
    form_class = ContactRequestForm
    template_name = 'contact/forms/request.html'

    def form_valid(self, form):
        response = super(ContactRequestView, self).form_valid(form)
        self.send_mail()
        return response

    def send_mail(self):
        send_request_email(self.get_form(), self.event)
        send_request_confirmation_email(self.get_form(), self.event)
