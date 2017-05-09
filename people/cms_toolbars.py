# -*- coding: utf-8 -*-
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from allink_core.allink_base.utils import AllinkBaseModifierMixin
from allink_core.allink_config.models import AllinkConfig
from allink_apps.people.models import People


class PeopleToolbar(AllinkBaseModifierMixin, CMSToolbar):
    model = People

if AllinkConfig.get_solo().people_toolbar_enabled:
    toolbar_pool.register(PeopleToolbar)
