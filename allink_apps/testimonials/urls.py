# # -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import TestimonialPluginLoadMore, TestimonialDetail


urlpatterns = [
    url(r'^(?P<page>[0-9]*)/$', TestimonialPluginLoadMore.as_view(), name='more'),
    url(r'^(?P<slug>[\w-]+)/$', TestimonialDetail.as_view(), name='detail'),
]
