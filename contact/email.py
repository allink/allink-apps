# -*- coding: utf-8 -*-
from django.template.loader import render_to_string
from django.conf import settings

from allink_core.allink_base.utils import get_display
from allink_core.allink_mandrill.config import MandrillConfig
from allink_core.allink_mandrill.helpers import send_transactional_email

config = MandrillConfig()


def send_request_email(form, plugin):
    subject = render_to_string('contact/email/request_subject_internal.txt')
    template_content = [{}]

    r = '<br />'
    data = []
    for field in form.fields:
        if field != 'terms' and field != 'terms_accepted':
            if form.data.get(field):
                if hasattr(form.fields.get(field), 'choices'):
                    data.append((form.fields.get(field).label, get_display(form.data.get(field), form.fields.get(field).choices)))
                else:
                    data.append((form.fields.get(field).label, form.data.get(field)))

    subscriber = render_to_string('contact/email/request_subscriber.txt', {'data': data})
    subscriber = subscriber.replace('\r\n', r).replace('\n\r', r).replace('\r', r).replace('\n', r)
    # subscriber = subscriber.encode('utf-8')

    message = {
        'auto_html': None,
        'auto_text': None,
        'from_email': plugin.from_email_address if plugin and plugin.from_email_address else settings.CONTACT_REQUEST_EMAIL,
        'from_name': config.get_default_from_name(),
        'global_merge_vars': [
            {'name': 'detail_link', 'content': u'hello'},
            {'name': 'subscriber', 'content': subscriber}
        ],
        'headers': {'Reply-To': plugin.from_email_address if plugin and plugin.from_email_address else settings.CONTACT_REQUEST_EMAIL},
        'inline_css': True,
        'merge': True,
        'merge_language': 'mailchimp',
        'metadata': {'website': config.get_site_domain()},
        'preserve_recipients': True,
        'return_path_domain': None,
        'subject': subject,
        'to': [{
            'email': email_address,
            'name': config.get_default_from_name(),
            'type': 'to'
        } for email_address in plugin.internal_email_adresses if email_address] if plugin and plugin.internal_email_adresses else [{
            'email': config.default_to_email,
            'name': config.get_default_from_name(),
            'type': 'to'
        }],
        'track_clicks': True,
        'track_opens': True
    }
    send_transactional_email(message=message, template_name='hrcampus_request_internal_de', template_content=template_content)


def send_request_confirmation_email(form, plugin):
    subject = render_to_string('contact/email/request_subject.txt')
    template_content = [{}]

    r = '<br />'
    data = []
    for field in form.fields:
        if field != 'terms' and field != 'terms_accepted':
            if form.data.get(field):
                if hasattr(form.fields.get(field), 'choices'):
                    data.append((form.fields.get(field).label,
                                 get_display(form.data.get(field), form.fields.get(field).choices)))
                else:
                    data.append((form.fields.get(field).label, form.data.get(field)))

    subscriber = render_to_string('contact/email/request_subscriber.txt', {'data': data})
    subscriber = subscriber.replace('\r\n', r).replace('\n\r', r).replace('\r', r).replace('\n', r)

    message = str(form.fields.get('message')).replace('\r\n', r).replace('\n\r', r).replace('\r', r).replace('\n', r)

    message = {
        'auto_html': None,
        'auto_text': None,
        'from_email': plugin.from_email_address if plugin and plugin.from_email_address else settings.CONTACT_REQUEST_EMAIL,
        'from_name': config.get_default_from_name(),
        'global_merge_vars': [
            {'name': 'first_name', 'content': form.data.get('first_name')},
            {'name': 'last_name', 'content': form.data.get('last_name')},
            {'name': 'subscriber', 'content': subscriber},
            {'name': 'message', 'content': message}
        ],
        'google_analytics_campaign': 'Contact Request',
        'google_analytics_domains': [config.get_google_analytics_domains()],
        'headers': {'Reply-To': plugin.from_email_address if plugin and plugin.from_email_address else config.default_from_email},
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
    send_transactional_email(message=message, template_name='hrcampus_request_confirmation', translated=True, template_content=template_content)
