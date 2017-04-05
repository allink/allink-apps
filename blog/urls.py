# # -*- coding: utf-8 -*-
from django.conf.urls import url
from allink_apps.blog.views import BlogPluginLoadMore, BlogDetail, EventsRegistrationView


urlpatterns = [
    url(r'^(?P<page>[0-9]*)/$', BlogPluginLoadMore.as_view(), name='more'),
    url(r'^(?P<slug>[\w-]+)/$', BlogDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/register/$', EventsRegistrationView.as_view(), name='register'),
]
