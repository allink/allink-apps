# # -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import ContactRequestView


urlpatterns = [
    url(r'^request/$', ContactRequestView.as_view(), name='request'),
]
