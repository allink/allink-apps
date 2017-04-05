# -*- coding: utf-8 -*-
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from allink_core.allink_base.utils import AllinkBaseModifierMixin

from allink_apps.work.models import Work


@toolbar_pool.register
class WorkToolbar(AllinkBaseModifierMixin, CMSToolbar):
    model = Work
    app_label = Work._meta.app_label
