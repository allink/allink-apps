# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from allink_core.allink_base.forms import AllinkBaseModelForm
from allink_core.allink_terms.models import AllinkTerms

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
        try:
            self.fields['terms_accepted'].label = mark_safe(_('I have read and accept the <a href="%s" target="_blank">terms and conditions.</a>')) % \
                                              (AllinkTerms.objects.get_published().terms_cms_page.get_absolute_url())
        except:
            raise AttributeError(_(u'Please configure Terms. And create the corresponding cms Page.'))

        #  all fiels should be required
        for key in self.fields:
            if key != 'message':
                self.fields[key].required = True
