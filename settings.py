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
    'djangocms-picture',
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
from allink_core.allink_config.allink_settings import ALLINK_INSTALLED_APPS, \
    ALLINK_PROJECT_APP_MODEL_WITH_CATEGORY_CHOICES, ALLINK_CMS_PLACEHOLDER_CONF_PLUGINS,\
    ALLINK_MIGRATION_MODULES, CMS_ALLINK_CONTENT_PLUGIN_CHILD_CLASSES, ALLINK_MIDDLEWARE_CLASSES
from django.utils.translation import ugettext_lazy as _

aldryn_addons.settings.load(locals())

gettext = lambda s: s

####################################################################################

# Installed =Apps

INSTALLED_APPS.extend(ALLINK_INSTALLED_APPS)


# project specific apps
PROJECT_APPS = [
    # 'apps.courses',
]

INSTALLED_APPS.extend(PROJECT_APPS)

####################################################################################

# =Migration Modlues allink apps

MIGRATION_MODULES = ALLINK_MIGRATION_MODULES

####################################################################################

# =Middleware
MIDDLEWARE_CLASSES.extend(ALLINK_MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES.extend([
    # add your own middlewares here
])

####################################################################################

# =Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIRS, os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'django.core.context_processors.static',
                'aldryn_django.context_processors.debug',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'aldryn_boilerplates.context_processors.boilerplate',
                'aldryn_snake.template_api.template_processor',
                'django.template.context_processors.request',
                'allink_core.allink_config.context_processors.allink_config',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ]
        },
    }
]

####################################################################################

# =Templates

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)



####################################################################################

# =allauth

ACCOUNT_ADAPTER = 'allink_apps.members.allauth_adapter.AccountAdapter'
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
####################################################################################

MEMBERS_INITIAL_PWD = '123'

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
    'startupOutlineBlocks': 'false',
    'forcePasteAsPlainText': 'true',
    'skin': 'moono',
    'height': 400,
    'language': '{{ language }}',
    # toolbar for the default text plugin
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Styles', 'Bold', 'Italic', '-', 'RemoveFormat'],
        ['NumberedList', 'BulletedList'],
        ['Source'],
    ],
    # toolbar when using the HTMLField in a models.py
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['ShowBlocks'],
        ['Styles', 'Bold', 'Italic', '-', 'RemoveFormat'],
        ['NumberedList', 'BulletedList'],
        ['Source'],

    ],
    'stylesSet': [
        # {
        #     'name': 'Display Titel',
        #     'element': 'h1',
        #     'attributes': {
        #         'class': 'display-1',
        #     }
        # },
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
# -> add project specific plugins to ALLINK_CMS_PLACEHOLDER_CONF_PLUGINS

# ALLINK_CMS_PLACEHOLDER_CONF_PLUGINS.append('CMSCoursesPlugin')

CMS_PLACEHOLDER_CONF = {
    'content': {
        "plugins": ALLINK_CMS_PLACEHOLDER_CONF_PLUGINS,
        'exclude_plugins': ['InheritPlugin'],
    },
    'social_profiles': {
        "plugins": ['CMSAllinkSocialIconContainerPlugin'],
        'exclude_plugins': ['InheritPlugin'],
    },
    'service_navigation': {
        "plugins": ['CMSAllinkButtonLinkContainerPlugin'],
        'exclude_plugins': ['InheritPlugin'],
    },
    'footer_content': {
        "plugins": ['CMSAllinkContentPlugin', 'TextPlugin'],
        'exclude_plugins': ['InheritPlugin'],
    },
    'map': {
        "plugins": ['CMSLocationsPlugin'],
        'exclude_plugins': ['InheritPlugin'],
    },
    'blog_content': {
        "plugins": ['TextPlugin', 'CMSAllinkImagePlugin', 'VideoPlayerPlugin'],
        'exclude_plugins': ['InheritPlugin'],
    },
    'blog_header': {
        "plugins": ['CMSAllinkImagePlugin', 'CMSAllinkGalleryPlugin'],
        'exclude_plugins': ['InheritPlugin'],
    }
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
# MAILCHIMP_MERGE_VARS = ''
# MAILCHIMP_DOUBLE_OPTIN = '' # DEFAULT: True

# =MANDRILL CONFIG
MANDRILL_API_KEY = senv('MANDRILL_API_KEY')

EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'allink'
EMAIL_HOST_PASSWORD = senv('MANDRILL_API_KEY')
DEFAULT_FROM_EMAIL = senv('DEFAULT_FROM_EMAIL')

# =GOOGLE TAG MANAGER CONFIG
GOOGLE_TAG_MANAGER_ID = senv('GOOGLE_TAG_MANAGER_ID')

# =GOOGLE MAP API KEY
GOOGLE_MAP_API_KEY = senv('GOOGLE_MAP_API_KEY')

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

####################################################################################

# = allink categories
# all models which use categories have to be listed here.
# the value has to be equal to "_meta.model_name"
# -> Overeride if project specific setup requires

PROJECT_APP_MODEL_WITH_CATEGORY_CHOICES = ALLINK_PROJECT_APP_MODEL_WITH_CATEGORY_CHOICES

PROJECT_APP_MODEL_WITH_CATEGORY_CHOICES.extend([
    # ('courses', 'Courses'),
])



####################################################################################

# =allink app_content additional templates for apps
# the variable name prefix 'PEOPLE' in 'PEOPLE_PLUGIN_TEMPLATES' has to be equal to "_meta.model_name"
#

PEOPLE_PLUGIN_TEMPLATES = [
    ('table', 'Table (Alumni)'),
    ('table_2', 'Table (Dozent)'),
]


####################################################################################

# =CMSAllinkContentPlugin

PROJECT_COLORS = (
    'project-color-1',
    'project-color-2',
    'project-color-3',
)

CMS_ALLINK_CONTENT_PLUGIN_CHILD_CLASSES = CMS_ALLINK_CONTENT_PLUGIN_CHILD_CLASSES

####################################################################################

# =CMSAllinkGroupPlugin

CMS_ALLINK_GROUP_PLUGIN_CHILD_CLASSES = [
    # 'TextPlugin',
    # 'CMSAllinkImagePlugin',
    'CMSAllinkButtonLinkContainerPlugin',
    'CMSAllinkButtonLinkPlugin',
]

####################################################################################

# =allink Icon Set

PROJECT_ICONSETS = (
    ('glyphicons', 'glyphicons', 'Glyphicons'),
    ('fontawesome', 'fa', 'Fontawesome'),
)


####################################################################################

# =Custom Thumbnail Sizes

# Default thumbnail sizes are set in allink_core.allink_base.settings.easy_thumbnail.
# This is an example how you can modify existing sizes.
# -> Overeride if project specific setup requires

# Full list of sizes:
# https://github.com/allink/allink-core/blob/master/allink_core/allink_config/easy_thumbnail.py

# THUMBNAIL_ALIASES['']['col-3-of-3-xs'] = {'size': (450, get_height_from_ratio(450,2,1)), 'crop': 'smart', 'upscale': True}
# THUMBNAIL_ALIASES['']['col-3-of-3-xs-2x'] = {'size': (600, get_height_from_ratio(600,2,1)), 'crop': 'smart', 'upscale': True}
# THUMBNAIL_ALIASES['']['col-3-of-3-sm'] = {'size': (1200, get_height_from_ratio(1200,2,1)), 'crop': 'smart', 'upscale': True}
# THUMBNAIL_ALIASES['']['col-3-of-3-sm-2x'] = {'size': (1800, get_height_from_ratio(1800,2,1)), 'crop': 'smart', 'upscale': True}
# THUMBNAIL_ALIASES['']['col-3-of-3-xl'] = {'size': (1500, get_height_from_ratio(1500,2,1)), 'crop': 'smart', 'upscale': True}
# THUMBNAIL_ALIASES['']['col-3-of-3-xl-2x'] = {'size': (2500, get_height_from_ratio(2500,2,1)), 'crop': 'smart', 'upscale': True}
