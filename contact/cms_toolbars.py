# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from allink_core.allink_config.models import AllinkConfig
from allink_apps.contact.models import ContactRequest


class ContactToolbar(CMSToolbar):
    model = ContactRequest

    def populate(self):
        menu = self.toolbar.get_or_create_menu('form-menu', _('Forms'))

        url = reverse('admin:{}_{}_changelist'.format(self.model._meta.app_label, self.model._meta.model_name))
        menu.add_sideframe_item(self.model.get_verbose_name_plural(), url=url)


if AllinkConfig.get_solo().contact_toolbar_enabled:
    toolbar_pool.register(ContactToolbar)
