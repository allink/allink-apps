# -*- coding: utf-8 -*-
import datetime
from django import forms
from django.utils.translation import ugettext_lazy as _

from allink_core.allink_base.forms import AllinkBaseModelForm

from allink_apps.contact.models import ContactRequest


class ContactRequestBaseForm(AllinkBaseModelForm):

    email = forms.CharField(
        label=_(u'E-Mail'),
        required=False
    )
    date = forms.DateField(
            label=_(u'Date'),
            widget=forms.TextInput(
                attrs={
                    'class': 'datepicker',
                    'placeholder': _(u'Please choose a date.')
                }),
        required=False
    )

    class Meta:
        model = None
        fields = ('salutation', 'first_name', 'last_name', 'company_name', 'contact_type', 'email', 'message', 'phone', 'date', 'time')

    def clean_date(self):
        date = self.cleaned_data['date']
        contact_type = self.cleaned_data.get('contact_type')
        if date and date < datetime.date.today():
            raise forms.ValidationError(_(u'Date has to be in the future.'))

        if contact_type == ContactRequest.CONTACT_PHONE and not date:
            raise forms.ValidationError(_(u'This field is required.'))
        return date

    def clean_phone(self):
        contact_type = self.cleaned_data.get('contact_type')
        phone = self.cleaned_data['phone']
        if contact_type == ContactRequest.CONTACT_PHONE and not phone:
            raise forms.ValidationError(_(u'This field is required.'))
        return phone

    def clean_time(self):
        contact_type = self.cleaned_data.get('contact_type')
        time = self.cleaned_data['time']
        if contact_type == ContactRequest.CONTACT_PHONE and not time:
            raise forms.ValidationError(_(u'This field is required.'))
        return time

    def clean_email(self):
        contact_type = self.cleaned_data.get('contact_type')
        email = self.cleaned_data['email']
        if contact_type == ContactRequest.CONTACT_EMAIL and not email:
            raise forms.ValidationError(_(u'This field is required.'))
        return email


class ContactRequestForm(ContactRequestBaseForm):

    class Meta:
        model = ContactRequest
        fields = ('salutation', 'first_name', 'last_name', 'company_name', 'contact_type', 'email', 'message', 'phone', 'date', 'time')
