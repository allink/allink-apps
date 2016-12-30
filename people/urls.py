# # -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import PeoplePluginLoadMore, PeopleDetail


urlpatterns = [
    # url(r'^$', PeopleIndex.as_view(), name='index'),
    url(r'^(?P<page>[0-9]*)/$', PeoplePluginLoadMore.as_view(), name='more'),
    url(r'^(?P<slug>[\w-]+)/$', PeopleDetail.as_view(), name='detail'),
]
