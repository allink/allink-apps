# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_image', '0004_auto_20170303_0729'),
        ('blog', '0009_auto_20170306_0428'),
    ]

    operations = [
        migrations.RunSQL('''
            drop table if exists djangocms_picture_picture;
            delete from auth_permission where content_type_id in (select id from django_content_type where app_label = '{app_label}');
            delete from django_admin_log where content_type_id in (select id from django_content_type where app_label = '{app_label}');
            delete from reversion_version where content_type_id in (select id from django_content_type where app_label = '{app_label}');
            delete from django_content_type where app_label = '{app_label}';
            delete from django_migrations where app='{app_label}';
            '''.format(app_label='djangocms_picture'))
    ]
