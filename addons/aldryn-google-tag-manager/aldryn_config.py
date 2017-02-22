# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from aldryn_client import forms


class Form(forms.BaseForm):

    google_tag_manager_id = forms.CharField(
        "Google Tag Manager ID",
        required=False,
        initial='',
        help_text="Provide the Google Tag Manager ID for this site."
    )

    def to_settings(self, cleaned_data, settings_dict):
        if cleaned_data['google_tag_manager_id']:
            settings_dict['GOOGLE_TAG_MANAGER_ID'] = cleaned_data['google_tag_manager_id']

        return settings_dict
