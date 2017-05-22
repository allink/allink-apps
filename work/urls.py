# # -*- coding: utf-8 -*-
from django.conf.urls import url
from allink_apps.work.views import WorkPluginLoadMore, WorkDetail, export_pdf


urlpatterns = [
    # url(r'^$', WorkIndex.as_view(), name='index'),
    url(r'^(?P<page>[0-9]*)/$', WorkPluginLoadMore.as_view(), name='more'),
    url(r'^(?P<slug>[\w-]+)/$', WorkDetail.as_view(), name='detail'),
    url(r'^export-pdf/(?P<id>[0-9]+)/$', export_pdf, name='export-pdf'),
]
