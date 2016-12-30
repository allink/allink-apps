# -*- coding: utf-8 -*-

from allink_core.allink_base.views import AllinkBasePluginLoadMoreView, AllinkBaseDetailView
from .models import Testimonial, TestimonialAppContentPlugin


class TestimonialPluginLoadMore(AllinkBasePluginLoadMoreView):
    model = Testimonial
    plugin_model = TestimonialAppContentPlugin


class TestimonialDetail(AllinkBaseDetailView):
    template_name = 'testimonials/detail.html'
    model = Testimonial

