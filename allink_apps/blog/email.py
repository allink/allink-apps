# -*- coding: utf-8 -*-
from django.template.loader import render_to_string

from allink_core.allink_base.utils import base_url
from allink_core.allink_mandrill.config import MandrillConfig
from allink_core.allink_mandrill.helpers import send_transactional_email

config = MandrillConfig()


def send_registration_email(form, event):
    subject = render_to_string('events/email/registration_subject_internal.txt')
    template_content = [{}]

    r = '<br />'
    data = []
    for field in form.fields:
        if field != 'terms' and field != 'terms_accepted':
            if field == 'event':
                data.append((form.fields.get(field).label, event.title))
            else:
                data.append((form.fields.get(field).label, form.data.get(field)))

    subscriber = render_to_string('events/email/registration_subscriber.txt', {'data': data})
    subscriber = subscriber.replace('\r\n', r).replace('\n\r', r).replace('\r', r).replace('\n', r)
    subscriber = subscriber.encode('utf-8')

    message = {
        'auto_html': None,
        'auto_text': None,
        'from_email': config.default_from_email,
        'from_name': config.get_default_from_name(),
        'global_merge_vars': [
            {'name': 'detail_link', 'content': u'{}{}'.format(base_url(), event.get_absolute_url())},
            {'name': 'subscriber', 'content': subscriber}
        ],
        'headers': {'Reply-To': config.default_from_email},
        'inline_css': True,
        'merge': True,
        'merge_language': 'mailchimp',
        'metadata': {'website': config.get_site_domain()},
        'preserve_recipients': True,
        'return_path_domain': None,
        'subject': subject,
        'to': [{
            'email': config.default_to_email,
            'name': config.get_default_from_name(),
            'type': 'to'
        }],
        'track_clicks': True,
        'track_opens': True
    }
    send_transactional_email(message=message, template_name='hdf_registration_internal', template_content=template_content)


def send_registration_confirmation_email(form, event):
    subject = render_to_string('events/email/registration_subject.txt')
    template_content = [{}]

    message = {
        'auto_html': None,
        'auto_text': None,
        'from_email': config.default_from_email,
        'from_name': config.get_default_from_name(),
        'global_merge_vars': [
            {'name': 'first_name', 'content': form.data.get('first_name')},
            {'name': 'last_name', 'content': form.data.get('last_name')},
            {'name': 'detail_link', 'content': '{}{}'.format(base_url(), event.get_absolute_url())},
        ],
        'google_analytics_campaign': 'Event Registration',
        'google_analytics_domains': [config.get_google_analytics_domains()],
        'headers': {'Reply-To': config.default_from_email},
        'inline_css': True,
        'merge': True,
        'merge_language': 'mailchimp',
        'metadata': {'website': config.get_site_domain()},
        'preserve_recipients': True,
        'return_path_domain': None,
        'subject': subject,
        'to': [{
            'email': form.data.get('email'),
            'name': u'{} {}'.format(form.data.get('first_name'), form.data.get('last_name')),
            'type': 'to'
        }],
        'track_clicks': True,
        'track_opens': True
    }
    send_transactional_email(message=message, template_name='hdf_event_confirmation', translated=True, template_content=template_content)
