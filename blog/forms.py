# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from allink_core.allink_base.forms import AllinkBaseModelForm

from .models import EventsRegistration

class EventsRegistrationForm(AllinkBaseModelForm):
    terms_accepted = forms.BooleanField(label=_(u'Terms of Service'), required=True)

    class Meta:
        model = EventsRegistration
        widgets = {
            'event': forms.HiddenInput(),
            'terms': forms.HiddenInput(),
            'terms_accepted': forms.CheckboxInput()
        }
        fields = ('event', 'terms', 'first_name', 'last_name', 'email', 'street', 'zip_code', 'place', 'message', 'terms_accepted')

    def __init__(self, *args, **kwargs):
        super(EventsRegistrationForm, self).__init__(*args, **kwargs)
        #  all fiels should be required
        for key in self.fields:
            self.fields[key].required = True
