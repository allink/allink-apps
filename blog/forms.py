# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from allink_core.allink_base.forms import AllinkBaseModelForm

from .models import EventsRegistration

class EventsRegistrationForm(AllinkBaseModelForm):
    # event = forms.HiddenInput()

    class Meta:
        model = EventsRegistration
        fields = ('event', 'first_name', 'last_name', 'email', 'street', 'zip_code', 'place',)

    def save(self, commit=True):
        super(EventsRegistrationForm, self).save(commit=True)

