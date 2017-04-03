# -*- coding: utf-8 -*-
from django.views.generic import ListView
from allink_core.allink_base.views import AllinkBasePluginLoadMoreView, AllinkBaseDetailView

from .models import People, PeopleAppContentPlugin

class PeoplePluginLoadMore(AllinkBasePluginLoadMoreView):
    model = People
    plugin_model = PeopleAppContentPlugin

# class PeopleDetail(AllinkBaseDetailView):
#     model = People
