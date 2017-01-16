# -*- coding: utf-8 -*-
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from allink_core.allink_base.utils import AllinkBaseModifierMixin

from .models import Brands


@toolbar_pool.register
class BrandsModifier(AllinkBaseModifierMixin, CMSToolbar):
    model = Brands
    app_label = Brands._meta.app_label
