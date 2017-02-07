# -*- coding: utf-8 -*-
import requests
from django.utils.translation import ugettext_lazy as _
from allink_core.allink_mailchimp.helpers import list_members_put, list_members_delete, get_status_if_new
from allink_core.allink_mailchimp.config import MailChimpConfig


config = MailChimpConfig()

def update_mailchimp_list_member(member):
    # update mailchimp list
    data = {
        'email_address': member.email,
        'status': 'subscribed',
        'status_if_new': get_status_if_new(),
        'language': member.language,
        'merge_fields': {
            'FNAME': member.first_name,
            'LNAME': member.last_name
        }
    }
    if config.merge_vars:
        data = data.append(config.merge_vars)
    list_members_put(data)


def update_mailchimp_email_adress(old_email, member):
    # update mailchimp list when email changed
    # update existing or create new
    data = {
        'email_address': member.email,
        'status': 'subscribed',
        'status_if_new': get_status_if_new(),
        'language': member.language,
        'merge_fields': {
            'FNAME': member.first_name,
            'LNAME': member.last_name
        }
    }

    if config.merge_vars:
        data = data.append(config.merge_vars)
    list_members_put(data)
    # delete old member
    data = {
        'email_address': old_email,
        'status': 'unsubscribed',
        'language': member.language,
        'merge_fields': {
            'FNAME': member.first_name,
            'LNAME': member.last_name
        }
    }
    if config.merge_vars:
        data = data.append(config.merge_vars)
    list_members_delete(data)
