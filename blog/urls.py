# # -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import BlogPluginLoadMore, BlogDetail, EventRegister


urlpatterns = [
    url(r'^(?P<page>[0-9]*)/$', BlogPluginLoadMore.as_view(), name='more'),
    url(r'^(?P<slug>[\w-]+)/$', BlogDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/register/$', EventRegister.as_view(), name='register'),
]
