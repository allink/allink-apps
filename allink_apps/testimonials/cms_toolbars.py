# -*- coding: utf-8 -*-
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from allink_core.allink_base.utils import AllinkBaseModifierMixin

from .models import Testimonial


@toolbar_pool.register
class TestimonialModifier(AllinkBaseModifierMixin, CMSToolbar):
    model = Testimonial
    app_label = Testimonial._meta.app_label
