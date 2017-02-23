# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from cms.plugin_pool import plugin_pool
from allink_core.allink_base.admin.cms_plugins import CMSAllinkBaseAppContentPlugin
from .models import BlogAppContentPlugin


@plugin_pool.register_plugin
class CMSBlogPlugin(CMSAllinkBaseAppContentPlugin):
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
    model = BlogAppContentPlugin
    name = model.data_model._meta.verbose_name_plural
    data_model = BlogAppContentPlugin.data_model

    @classmethod
    def get_render_queryset(cls):
        return cls.model._default_manager.all()

    # TODO
    # def get_render_template(self, context, instance, placeholder, file='content'):
    #     print self.data_model.__dict__
    #     if hasattr(self.data_model, 'events'):
    #         name = self.data_model.events._meta.model_name
    #     elif hasattr(self.data_model, 'news'):
    #         name = self.data_model.news._meta.model_name
    #     else:
    #         name = self.data_model._meta.model_name
    #
    #     template = '{}/plugins/{}/{}.html'.format(self.data_model._meta.app_label, name, instance.template, file)
    #     try:
    #         get_template(template)
    #     except TemplateDoesNotExist:
    #         template = 'app_content/plugins/{}/{}.html'.format(instance.template, file)
    #     return template
