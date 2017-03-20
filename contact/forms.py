# -*- coding: utf-8 -*-
import datetime
from django import forms
from django.utils.translation import ugettext_lazy as _

from allink_core.allink_base.forms import AllinkBaseModelForm

from .models import ContactRequest


class ContactRequestBaseForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker', 'placeholder': _(u'Please choose a date.')}), required=False)

    class Meta:
        model = None
        fields = ('first_name', 'last_name', 'email', 'message', 'contact_type', 'date', 'time')

    def clean_date(self):
        date = self.cleaned_data['date']
        contact_type = self.cleaned_data.get('contact_type')
        if date and date < datetime.date.today():
            raise forms.ValidationError(_(u'Date has to be in the future.'))

        if contact_type == ContactRequest.CONTACT_PHONE and not date:
            raise forms.ValidationError(_(u'This field is required.'))
        return date

    def clean_email(self):
        contact_type = self.cleaned_data.get('contact_type')
        email = self.cleaned_data['email']
        if contact_type == ContactRequest.CONTACT_EMAIL and not email:
            raise forms.ValidationError(_(u'This field is required.'))
        return email

    def clean_telephone(self):
        contact_type = self.cleaned_data.get('contact_type')
        telephone = self.cleaned_data['telephone']
        if contact_type == ContactRequest.CONTACT_PHONE and not telephone:
            raise forms.ValidationError(_(u'This field is required.'))
        return telephone

    def clean_time(self):
        contact_type = self.cleaned_data.get('contact_type')
        time = self.cleaned_data['time']
        if contact_type == ContactRequest.CONTACT_PHONE and not time:
            raise forms.ValidationError(_(u'This field is required.'))
        return time


class ContactRequestForm(AllinkBaseModelForm):

    class Meta:
        model = ContactRequest
        fields = ('first_name', 'last_name', 'email', 'message', 'contact_type', 'date', 'time')

    def __init__(self, *args, **kwargs):
        super(ContactRequestForm, self).__init__(*args, **kwargs)

        #  required fiels
        for key in self.fields:
            if key != 'message' and key != 'type' and key != 'date' and key != 'time':
                self.fields[key].required = True



