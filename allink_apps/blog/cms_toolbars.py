# -*- coding: utf-8 -*-
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from allink_core.allink_base.utils import AllinkBaseModifierMixin

from .models import News, Events


@toolbar_pool.register
class NewsModifier(AllinkBaseModifierMixin, CMSToolbar):
    model = News
    app_label = News._meta.app_label


@toolbar_pool.register
class EventsModifier(AllinkBaseModifierMixin, CMSToolbar):
    model = Events
    app_label = Events._meta.app_label


@toolbar_pool.register
class CoursesModifier(AllinkBaseModifierMixin, CMSToolbar):
    model = Courses
    app_label = Courses._meta.app_label
