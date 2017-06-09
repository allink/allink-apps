# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from allink_core.allink_base.utils import AllinkBaseModifierMixin
from allink_core.allink_config.models import AllinkConfig
from allink_apps.blog.models import News, Events, EventsRegistration

config = AllinkConfig.get_solo()


class NewsToolbar(AllinkBaseModifierMixin, CMSToolbar):
    model = News
    app_label = News._meta.app_label


if config.news_toolbar_enabled:
    toolbar_pool.register(NewsToolbar)


class EventsToolbar(AllinkBaseModifierMixin, CMSToolbar):
    model = Events
    app_label = Events._meta.app_label


if config.events_toolbar_enabled:
    toolbar_pool.register(EventsToolbar)


class EventsRegistrationToolbar(CMSToolbar):
    model = EventsRegistration

    def populate(self):
        menu = self.toolbar.get_or_create_menu('form-menu', _('Forms'))

        url = reverse('admin:{}_{}_changelist'.format(self.model._meta.app_label, self.model._meta.model_name))
        menu.add_sideframe_item(self.model.get_verbose_name_plural(), url=url)


if config.events_registration_toolbar_enabled:
    toolbar_pool.register(EventsRegistrationToolbar)
