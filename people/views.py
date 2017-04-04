# -*- coding: utf-8 -*-
from allink_core.allink_base.views import AllinkBasePluginLoadMoreView

from allink_apps.people.models import People, PeopleAppContentPlugin


class PeoplePluginLoadMore(AllinkBasePluginLoadMoreView):
    model = People
    plugin_model = PeopleAppContentPlugin

# class PeopleDetail(AllinkBaseDetailView):
#     model = People
