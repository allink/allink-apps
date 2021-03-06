# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class PeoplesApphook(CMSApp):
    name = _("People Apphook")
    app_name = 'people'

    def get_urls(self, page=None, language=None, **kwargs):
        return ['allink_apps.people.urls']


apphook_pool.register(PeoplesApphook)
