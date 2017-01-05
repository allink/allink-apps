# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from allink_core.allink_base.views import AllinkBasePluginLoadMoreView, AllinkBaseDetailView
from .models import Blog, BlogAppContentPlugin


class BlogPluginLoadMore(AllinkBasePluginLoadMoreView):
    model = Blog
    plugin_model = BlogAppContentPlugin


class BlogDetail(AllinkBaseDetailView):
    model = Blog

    def get_template_names(self):
        names = []
        if hasattr(self.object, 'events'):
            name = self.object.events._meta.model_name
        elif hasattr(self.object, 'news'):
            name = self.object.news._meta.model_name
        else:
            name = self.object._meta.model_name

        names.append("%s/%s%s.html" % (
            self.object._meta.app_label,
            name,
            self.template_name_suffix
        ))
        return names
