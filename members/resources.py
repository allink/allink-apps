# -*- coding: utf-8 -*-
from import_export import resources
from allink_apps.members.models import Members


class MembersResource(resources.ModelResource):

    class Meta:
        model = Members
        skip_unchanged = True
        report_skipped = False
        fields = ('member_nr', 'first_name', 'last_name', 'email')
        import_id_fields = ['member_nr']
        exclude_header = ('id')
