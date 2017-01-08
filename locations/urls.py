# # -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import LocationsPluginLoadMore, LocationsDetail


urlpatterns = [
    # url(r'^$', WorkIndex.as_view(), name='index'),
    url(r'^(?P<page>[0-9]*)/$', LocationsPluginLoadMore.as_view(), name='more'),
    url(r'^(?P<slug>[\w-]+)/$', LocationsDetail.as_view(), name='detail'),
]
