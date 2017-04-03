# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.sitemaps import Sitemap
from ..models import Testimonial


class TestimonialSitemap(Sitemap):

    changefreq = "never"
    priority = 0.5
    i18n = True

    def __init__(self, *args, **kwargs):
        self.namespace = kwargs.pop('namespace', None)
        super(TestimonialSitemap, self).__init__(*args, **kwargs)

    def items(self):
        return Testimonial.objects.active()

    def lastmod(self, obj):
        return obj.modified
