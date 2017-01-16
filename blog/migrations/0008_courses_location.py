# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0010_auto_20170111_0250'),
        ('blog', '0007_auto_20170110_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='location',
            field=models.ForeignKey(blank=True, to='locations.Locations', null=True),
        ),
    ]
