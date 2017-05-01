# -*- coding: utf-8 -*-
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from allink_core.allink_base.admin.cms_plugins import CMSAllinkBaseAppContentPlugin
from allink_apps.locations.models import LocationsAppContentPlugin


from django.template.loader import get_template
from django.template import TemplateDoesNotExist

@plugin_pool.register_plugin
class CMSLocationsPlugin(CMSAllinkBaseAppContentPlugin):
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
    model = LocationsAppContentPlugin
    name = model.data_model.get_verbose_name_plural()
    data_model = LocationsAppContentPlugin.data_model

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(CMSLocationsPlugin, self).get_fieldsets(request, obj=None)
        fieldsets += (_('Map Options'), {
            'classes': (
                'collapse',
                'only_when_map',
            ),
            'fields': (
                'zoom_level',
            )
        }),
        return fieldsets
