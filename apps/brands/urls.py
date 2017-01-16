# # -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import BrandsPluginLoadMore, BrandsDetail


urlpatterns = [
    url(r'^(?P<page>[0-9]*)/$', BrandsPluginLoadMore.as_view(), name='more'),
    url(r'^(?P<slug>[\w-]+)/$', BrandsDetail.as_view(), name='detail'),
]
