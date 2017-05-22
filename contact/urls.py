# # -*- coding: utf-8 -*-
from django.conf.urls import url
from allink_apps.contact.views import ContactRequestView


urlpatterns = [
    url(r'^request/$', ContactRequestView.as_view(), name='request'),
    url(r'^request/(?P<plugin_id>[0-9]+)/$', ContactRequestView.as_view(), name='plugin-request'),
]
