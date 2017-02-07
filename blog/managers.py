# -*- coding: utf-8 -*-
from allink_core.allink_base.models.managers import AllinkBaseModelQuerySet, AllinkBaseModelManager


class AllinkEventsQuerySet(AllinkBaseModelQuerySet):

    def latest(self):
        return self.order_by('event_date', 'id').distinct('event_date', 'id')

    def oldest(self):
        return self.order_by('-event_date', 'id').distinct('event_date', 'id')


class AllinkEventsManager(AllinkBaseModelManager):
    queryset_class = AllinkEventsQuerySet
