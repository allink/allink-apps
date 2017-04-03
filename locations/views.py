# -*- coding: utf-8 -*-

from allink_core.allink_base.views import AllinkBasePluginLoadMoreView, AllinkBaseDetailView
from .models import Locations, LocationsAppContentPlugin


class LocationsPluginLoadMore(AllinkBasePluginLoadMoreView):
    model = Locations
    plugin_model = LocationsAppContentPlugin


class LocationsDetail(AllinkBaseDetailView):
    model = Locations

