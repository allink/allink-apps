# -*- coding: utf-8 -*-
from allink_core.allink_base.models.managers import AllinkBaseModelQuerySet, AllinkBaseModelManager


class AllinkTestimonialQuerySet(AllinkBaseModelQuerySet):

    def title_asc(self):
        return self.translated().order_by('translations__lastname', 'id').distinct('translations__lastname', 'id')

    def title_desc(self):
        return self.translated().order_by('-translations__lastname', 'id').distinct('translations__lastname', 'id')


class AllinkTestimonialManager(AllinkBaseModelManager):
    queryset_class = AllinkTestimonialQuerySet
