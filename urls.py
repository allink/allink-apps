# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls


urlpatterns = [
    # add your own patterns here
    url(r'^styleguide/', include('allink_core.allink_styleguide.urls', namespace='styleguide')),
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    url(r'^courses/', include('allink_apps.work.urls', namespace='work')),
    url(r'^people/', include('allink_apps.people.urls', namespace='people')),
    url(r'^testimonials/', include('allink_apps.testimonials.urls', namespace='testimonial')),
    url(r'^blog/', include('allink_apps.blog.urls', namespace='blog')),
    url(r'^locations/', include('allink_apps.locations.urls', namespace='locations')),
    url(r'^plugin_forms/', include('cmsplugin_form_handler.urls',
                                   namespace='cmsplugin_form_handler')),
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
