# coding=utf-8
from django import forms
from parler.forms import TranslatableModelForm
from allink_apps.members.models import Members


class MembersAdminForm(TranslatableModelForm):

    class Meta:
        model = Members
        fields = ('member_nr', 'first_name', 'last_name', 'email', 'language')


class MemberProfileEditForm(forms.ModelForm):

    class Meta:
        model = Members
        fields = ('email', )
