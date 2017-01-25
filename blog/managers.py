# -*- coding: utf-8 -*-
from allink_core.allink_base.models.managers import AllinkBaseModelQuerySet, AllinkBaseModelManager


class AllinkEventQuerySet(AllinkBaseModelQuerySet):

    def latest(self):
        return self.order_by('-event_date', 'id').distinct('event_date', 'id')

    def oldest(self):
        return self.order_by('event_date', 'id').distinct('event_date', 'id')


class AllinkEventManager(AllinkBaseModelManager):
    queryset_class = AllinkEventQuerySet
