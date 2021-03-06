# # -*- coding: utf-8 -*-
from django.conf.urls import url
from allink_apps.blog.views import EventsPluginLoadMore, EventsDetail, EventsRegistrationView


urlpatterns = [
    url(r'^(?P<page>[0-9]*)/$', EventsPluginLoadMore.as_view(), name='more'),
    url(r'^(?P<slug>[\w-]+)/$', EventsDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/register/$', EventsRegistrationView.as_view(), name='register'),
]
