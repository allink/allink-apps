# -*- coding: utf-8 -*-
from datetime import date
from django.db.models import Q
from polymorphic.query import PolymorphicQuerySet
from polymorphic.manager import PolymorphicManager
from allink_core.allink_base.models.managers import AllinkBaseModelQuerySet, AllinkBaseModelManager


class AllinkBlogQuerySet(AllinkBaseModelQuerySet, PolymorphicQuerySet):
    def active_entries(self):
        '''
         entries which are active
        '''
        today = date.today()
        return self.translated().filter(Q(is_active=True) & (Q(start__isnull=True) & Q(end__isnull=True)) | ((Q(start__lte=today) & Q(end__isnull=True)) | (Q(start__isnull=True) & Q(end__gte=today))) | (Q(start__lte=today) & Q(end__gte=today)))


class AllinkBlogManager(PolymorphicManager, AllinkBaseModelManager):
    queryset_class = AllinkBlogQuerySet


class AllinkEventsQuerySet(AllinkBaseModelQuerySet, PolymorphicQuerySet):
    def active_entries(self):
        '''
         entries which are active
        '''
        today = date.today()
        return self.translated().filter(Q(is_active=True) & (Q(start__isnull=True) & Q(end__isnull=True)) | ((Q(start__lte=today) & Q(end__isnull=True)) | (Q(start__isnull=True) & Q(end__gte=today))) | (Q(start__lte=today) & Q(end__gte=today)))

    def latest(self):
        return self.translated().order_by('event_date', 'id').distinct('event_date', 'id')

    def earliest(self):
        return self.translated().order_by('-event_date', 'id').distinct('event_date', 'id')


class AllinkEventsManager(PolymorphicManager, AllinkBaseModelManager):
    queryset_class = AllinkEventsQuerySet
