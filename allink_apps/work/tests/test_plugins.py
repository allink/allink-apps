# -*- coding: utf-8 -*-
import os
from django.test import TestCase
from django.test.client import RequestFactory
from django.template.loader import render_to_string

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer

import allink_apps.work as app
from allink_apps.work.cms_plugins import CMSWorkPlugin

APP_NAME = 'work'
TEMPLATE_DIR = os.path.join(os.path.dirname(app.__file__), 'templates', APP_NAME)

#
# class CMSWorkluginTest(TestCase):
#
#     def test_plugin_html(self):
#         placeholder = Placeholder.objects.create(slot='test')
#         model_instance = add_plugin(
#             placeholder,
#             CMSWorkPlugin,
#             'en',
#         )
#         renderer = ContentRenderer(request=RequestFactory())
#         html = renderer.render_plugin(model_instance, {})
#         self.assertEqual(html, render_to_string(os.path.join(TEMPLATE_DIR, 'content.html')))