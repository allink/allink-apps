# -*- coding: utf-8 -*-
from allink_core.allink_base.models.managers import AllinkBaseModelQuerySet, AllinkBaseModelManager


class AllinkTestimonialQuerySet(AllinkBaseModelQuerySet):

    def title_asc(self):
        return self.active_entries()\
            .order_by('firstname', 'id')\
            .distinct('firstname', 'id')

    def title_desc(self):
        return self.active_entries()\
            .order_by('-firstname', 'id')\
            .distinct('firstname', 'id')


class AllinkTestimonialManager(AllinkBaseModelManager):
    queryset_class = AllinkTestimonialQuerySet
