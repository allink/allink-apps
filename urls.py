# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from cms.sitemaps import CMSSitemap

from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls

from allink_apps.work.sitemaps import WorkSitemap
from allink_apps.testimonials.sitemaps import TestimonialSitemap
from allink_apps.people.sitemaps import PeopleSitemap
from allink_apps.locations.sitemaps import LocationsSitemap
from allink_apps.blog.sitemaps import BlogSitemap

sitemaps = {
    'cms': CMSSitemap,
    'locations': LocationsSitemap,
    'work': WorkSitemap,
    'testimonials': TestimonialSitemap,
    'people': PeopleSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    # add your own patterns here
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^styleguide/', include('allink_core.allink_styleguide.urls', namespace='styleguide')),
    url(r'^mailchimp/', include('allink_core.allink_mailchimp.urls', namespace='mailchimp')),


] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    # url(r'^plugin_forms/', include('cmsplugin_form_handler.urls', namespace='cmsplugin_form_handler')),

    # Override allauth views
    # url(r'^accounts/password/change/$', login_required(MembersChangePassword.as_view()), name='profile_edit'),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^members/', include('allink_apps.members.urls', namespace='members')),

    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
