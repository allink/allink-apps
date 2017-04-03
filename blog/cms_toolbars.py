# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from allink_core.allink_base.utils import AllinkBaseModifierMixin

from .models import News, Events, EventsRegistration


@toolbar_pool.register
class NewsToolbar(AllinkBaseModifierMixin, CMSToolbar):
    model = News
    app_label = News._meta.app_label


@toolbar_pool.register
class EventsToolbar(AllinkBaseModifierMixin, CMSToolbar):
    model = Events
    app_label = Events._meta.app_label


@toolbar_pool.register
class EventsRegistrationToolbar(CMSToolbar):
    model = EventsRegistration

    def populate(self):
        menu = self.toolbar.get_or_create_menu(
            'form-menu'.format(self.model._meta.model_name),
            _('Forms'.format(self.model._meta.verbose_name_plural))
        )

        url = reverse('admin:{}_{}_changelist'.format(self.model._meta.app_label, self.model._meta.model_name))
        menu.add_sideframe_item(self.model._meta.verbose_name_plural, url=url)

