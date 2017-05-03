# -*- coding: utf-8 -*-

from allink_core.allink_base.models.managers import AllinkBaseModelQuerySet, AllinkBaseModelManager


class AllinkPeopleQuerySet(AllinkBaseModelQuerySet):

    def title_asc(self):
        return self.active_entries()\
            .order_by('lastname', 'id')\
            .distinct('lastname', 'id')

    def title_desc(self):
        return self.active_entries()\
            .order_by('-lastname', 'id')\
            .distinct('lastname', 'id')


class AllinkPeopleManager(AllinkBaseModelManager):
    queryset_class = AllinkPeopleQuerySet
    use_for_related_fields = True
