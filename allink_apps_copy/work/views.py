# -*- coding: utf-8 -*-

from allink_core.allink_base.views import AllinkBasePluginLoadMoreView, AllinkBaseDetailView
from .models import Work, WorkAppContentPlugin


class WorkPluginLoadMore(AllinkBasePluginLoadMoreView):
    model = Work
    plugin_model = WorkAppContentPlugin


class WorkDetail(AllinkBaseDetailView):
    model = Work

