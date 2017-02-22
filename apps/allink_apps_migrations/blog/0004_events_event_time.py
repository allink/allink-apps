# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170125_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_time',
            field=models.TimeField(null=True, verbose_name='Event Time', blank=True),
        ),
    ]
