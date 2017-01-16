# -*- coding: utf-8 -*-

####################################################################################

# Installed =Addons

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    'aldryn-django-cms',
    'aldryn-devsync',
    'aldryn-common',
    'aldryn-google-tag-manager',
    'djangocms-file',
    'djangocms-googlemap',
    'djangocms-link',
    'djangocms-picture',
    'djangocms-snippet',
    'djangocms-text-ckeditor',
    'djangocms-video',
    'django-filer',
    # </INSTALLED_ADDONS>
]

import aldryn_addons.settings
import os
import raven

from aldryn_addons.utils import senv

from allink_core.allink_base.utils import get_height_from_ratio
from allink_core.allink_config.easy_thumbnail import THUMBNAIL_ALIASES
from django.utils.translation import ugettext_lazy as _

aldryn_addons.settings.load(locals())

gettext = lambda s: s

####################################################################################

# Installed =Apps

INSTALLED_APPS.extend([
    # apps
    'webpack_loader',
    'aldryn_bootstrap3',
    'cmsplugin_form_handler',
    'adminsortable',
    'sortedm2m',
    'solo',

    # allink core apps
    'allink_core.allink_base',
    'allink_core.allink_config',
    'allink_core.allink_categories',
    'allink_core.allink_mailchimp',
    'allink_core.allink_styleguide',

    # allink apps
    'allink_apps.locations',
    'allink_apps.people',
    'allink_apps.work',
    # 'allink_apps.testimonials',
    'allink_apps.blog',


    # allink core djangocms plugins
    'allink_core.djangocms_content',
    'allink_core.djangocms_gallery',
    'allink_core.djangocms_socialicon',

])

# project specific apps
PROJECT_APPS = [
    # 'apps.work',
]

INSTALLED_APPS.extend(PROJECT_APPS)

####################################################################################

# =Middleware

MIDDLEWARE_CLASSES.extend([
    # add your own middlewares here
])

####################################################################################

# =Languages

# Django Languages:
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-LANGUAGES

# Django CMS Languages:
# http://docs.django-cms.org/en/release-3.4.x/reference/configuration.html#std:setting-CMS_LANGUAGES


# LANGUAGE_CODE = 'de'
#
# LANGUAGES = [
#     ('de', gettext('Deutsch')),
# ]

# CMS_LANGUAGES = {
#     1: [
#         {
#             'code': 'de',
#             'name': gettext('Deutsch'),
#             'public': True,
#             'hide_untranslated': True,
#         },
#     ],
#     'default': {
#         'public': True,
#         'hide_untranslated': False,
#     }
# }

####################################################################################

# django CMS templates
# http://docs.django-cms.org/en/latest/how_to/templates.html

CMS_TEMPLATES = (
    ('fullwidth.html', _('Standard')),
    ('logo-addition-white.html', _('Logo Zusatz (weiss)')),
    ('logo-addition-black.html', _('Logo Zusatz (schwarz)')),
)

####################################################################################

# Allowed Video File Extensions

ALLOWED_VIDEO_EXTENSIONS = ['mp4']


####################################################################################

# =Editor Plugin
# Complete list of editor settings:
# http://docs.ckeditor.com/#!/api/CKEDITOR.config

CKEDITOR_SETTINGS = {
    'contentsCss': os.path.join(STATIC_URL, 'build/style.css'),
    'bodyClass': 'editor-body',
    'startupOutlineBlocks': 'true',
    'forcePasteAsPlainText': 'true',
    'skin': 'moono',
    'height': 400,
    'language': '{{ language }}',
    # toolbar for the default text plugin
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Styles', 'RemoveFormat'],
        ['NumberedList', 'BulletedList'],
        ['Source'],
    ],
    # toolbar when using the HTMLField in a models.py
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['ShowBlocks'],
        ['Styles', 'RemoveFormat'],
        ['NumberedList', 'BulletedList'],
        ['Source'],
    ],
    'stylesSet': [
        {
            'name': 'Display Titel',
            'element': 'h1',
            'attributes': {
                'class': 'display-1',
            }
        },
        {
            'name': 'Titel Gross',
            'element': 'h1',
        },
        {
            'name': 'Titel Mittel',
            'element': 'h2',
        },
        {
            'name': 'Titel Klein',
            'element': 'h3',
        },
        {
            'name': 'Text Gross',
            'element': 'p',
            'attributes': {
                'class': 'lead',
            }
        },
        {
            'name': 'Text Normal',
            'element': 'p',
        },
        {
            'name': 'Text Klein',
            'element': 'p',
            'attributes': {
                'class': 'small',
            }
        },
    ],

}

# https://github.com/divio/djangocms-text-ckeditor#configurable-sanitizer
TEXT_ADDITIONAL_TAGS = ('iframe',)
TEXT_ADDITIONAL_ATTRIBUTES = ('scrolling', 'allowfullscreen', 'frameborder')


####################################################################################

# Assign Plugins to =Placeholders

# http://docs.django-cms.org/en/develop/reference/configuration.html#cms-placeholder-conf

CMS_PLACEHOLDER_CONF = {
    'content': {
        "plugins": [
            'CMSAllinkContentPlugin',
            'CMSLocationsPlugin',
            'CMSPeoplePlugin',
            'CMSWorkPlugin',
            'CMSBlogPlugin',
        ],
        'exclude_plugins': ['InheritPlugin'],
    },
    'social_profiles': {
        "plugins": ['CMSAllinkLinkContainerPlugin'],
        'exclude_plugins': ['InheritPlugin'],
    },
    'footer_content': {
        "plugins": ['TextPlugin'],
        'exclude_plugins': ['InheritPlugin'],
    },
    'map': {
        "plugins": ['CMSLocationsPlugin'],
        'exclude_plugins': ['InheritPlugin'],
    },
}


####################################################################################

# Divio Environment Variables

# https://control.divio.com/

# =SENTRY CONFIG
RAVEN_CONFIG = {
    'dns': senv('SENTRY_DNS'),
}

# =MAILCHIMP CONFIG
MAILCHIMP_API_KEY = senv('MAILCHIMP_API_KEY')
MAILCHIMP_DEFAULT_LIST_ID = senv('MAILCHIMP_DEFAULT_LIST_ID')
# MAILCHIMP_SIGNUP_FORM = ''
# MAILCHIMP_DOUBLE_OPTIN = ''

# =GOOGLE TAG MANAGER CONFIG
GOOGLE_TAG_MANAGER_ID = senv('GOOGLE_TAG_MANAGER_ID')

# =GOOGLE MAP API KEY
GOOGLE_MAP_API_KEY = senv('GOOGLE_MAP_API_KEY')


####################################################################################

# = allink categories
# all models which use categories have to be listed here.
# the value has to be equal to "_meta.model_name"

PROJECT_APP_MODEL_WITH_CATEGORY_CHOICES = [
    ('people', 'People'),
    ('work', 'Work'),
    # ('testimonial', 'Testimonials'),
    ('blog', 'Blog'),
    ('news', 'News'),
    ('events', 'Events'),
    # ('courses', 'Courses'),
    # ('locations', 'Locations'),
]


####################################################################################

# =allink app_content additional templates for apps
# the variable name prefix 'PEOPLE' in 'PEOPLE_PLUGIN_TEMPLATES' has to be equal to "_meta.model_name"
#

PEOPLE_PLUGIN_TEMPLATES = [
    # ('table', 'Table (Alumni)'),
]


####################################################################################

# =allink content plugin

PROJECT_COLORS = (
    'project-color-1',
    'project-color-2',
    'project-color-3',
)


####################################################################################

# =Custom Thumbnail Sizes

# Default thumbnail sizes are set in allink_core.allink_base.settings.easy_thumbnail
# This is an example how you can modify existing sizes

# THUMBNAIL_ALIASES['']['col-3-of-3-xs'] = {'size': (450, get_height_from_ratio(450,2,1)), 'crop': 'smart'}
# THUMBNAIL_ALIASES['']['col-3-of-3-xs-2x'] = {'size': (600, get_height_from_ratio(600,2,1)), 'crop': 'smart'}
# THUMBNAIL_ALIASES['']['col-3-of-3-sm'] = {'size': (1200, get_height_from_ratio(1200,2,1)), 'crop': 'smart'}
# THUMBNAIL_ALIASES['']['col-3-of-3-sm-2x'] = {'size': (1800, get_height_from_ratio(1800,2,1)), 'crop': 'smart'}
# THUMBNAIL_ALIASES['']['col-3-of-3-xl'] = {'size': (1500, get_height_from_ratio(1500,2,1)), 'crop': 'smart'}
# THUMBNAIL_ALIASES['']['col-3-of-3-xl-2x'] = {'size': (2500, get_height_from_ratio(2500,2,1)), 'crop': 'smart'}
