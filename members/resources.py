# -*- coding: utf-8 -*-

from import_export import resources
from import_export import fields
from .models import Members

class MembersResource(resources.ModelResource):
    class Meta:
        model = Members
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'member_nr', 'first_name', 'last_name', 'email')
