# -*- coding: utf-8 -*-
from cms.plugin_pool import plugin_pool
from allink_core.allink_base.admin.cms_plugins import CMSAllinkBaseAppContentPlugin
from allink_apps.work.models import WorkAppContentPlugin


@plugin_pool.register_plugin
class CMSWorkPlugin(CMSAllinkBaseAppContentPlugin):
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
    model = WorkAppContentPlugin
    name = model.data_model.get_verbose_name_plural()
    data_model = WorkAppContentPlugin.data_model
