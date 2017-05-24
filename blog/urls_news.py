# # -*- coding: utf-8 -*-
from django.conf.urls import url
from allink_apps.blog.views import NewsPluginLoadMore, NewsDetail


urlpatterns = [
    url(r'^(?P<page>[0-9]*)/$', NewsPluginLoadMore.as_view(), name='more'),
    url(r'^(?P<slug>[\w-]+)/$', NewsDetail.as_view(), name='detail'),
]
