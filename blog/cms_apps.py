# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class BlogApphook(CMSApp):
    name = _("Blog Apphook")
    app_name = 'blog'

    def get_urls(self, page=None, language=None, **kwargs):
        return ['allink_apps.blog.urls']

apphook_pool.register(BlogApphook)
