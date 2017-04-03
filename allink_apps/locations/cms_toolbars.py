# -*- coding: utf-8 -*-
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from allink_core.allink_base.utils import AllinkBaseModifierMixin

from .models import Locations


@toolbar_pool.register
class LocationsToolbar(AllinkBaseModifierMixin, CMSToolbar):
    model = Locations
    app_label = Locations._meta.app_label
