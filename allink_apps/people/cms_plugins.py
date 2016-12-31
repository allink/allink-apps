# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from allink_core.allink_base.admin.cms_plugins import CMSAllinkBaseAppContentPlugin
from .models import People, PeopleAppContentPlugin


@plugin_pool.register_plugin
class CMSPeoplePlugin(CMSAllinkBaseAppContentPlugin):
    """
    Is only defined here because this Model is only for plugin instnances

    There should be no need to extend this Plugin with any logic. It is only registered here.

    model:
    - where to store plugin instances

    name:
    - name of the plugin

    data_model:
    - Where to get the data from
    (can also be a parent model, so automatically all subclasses will be selected)

    """
    model = PeopleAppContentPlugin
    name = model.data_model._meta.verbose_name_plural
    data_model = PeopleAppContentPlugin.data_model
