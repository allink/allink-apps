# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20170117_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='blog_ptr',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='location',
        ),
        migrations.AlterUniqueTogether(
            name='coursestranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='coursestranslation',
            name='master',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='internal',
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.DeleteModel(
            name='CoursesTranslation',
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
    ]
