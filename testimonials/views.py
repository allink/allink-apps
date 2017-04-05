# -*- coding: utf-8 -*-

from allink_core.allink_base.views import AllinkBasePluginLoadMoreView, AllinkBaseDetailView
from allink_apps.testimonials.models import Testimonial, TestimonialAppContentPlugin


class TestimonialPluginLoadMore(AllinkBasePluginLoadMoreView):
    model = Testimonial
    plugin_model = TestimonialAppContentPlugin


class TestimonialDetail(AllinkBaseDetailView):
    model = Testimonial
