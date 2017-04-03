# # -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import MembersIndex, MembersProfileEdit


urlpatterns = [
    url(r'^$', MembersIndex.as_view(), name='index'),
    url(r'^profile/edit/$', MembersProfileEdit.as_view(), name='profile_edit'),
]
