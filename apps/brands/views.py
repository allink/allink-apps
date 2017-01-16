# -*- coding: utf-8 -*-

from allink_core.allink_base.views import AllinkBasePluginLoadMoreView, AllinkBaseDetailView
from .models import Brands, BrandsAppContentPlugin


class BrandsPluginLoadMore(AllinkBasePluginLoadMoreView):
    model = Brands
    plugin_model = BrandsAppContentPlugin


class BrandsDetail(AllinkBaseDetailView):
    model = Brands

