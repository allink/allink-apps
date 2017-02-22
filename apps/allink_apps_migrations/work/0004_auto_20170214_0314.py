# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_auto_20170125_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workappcontentplugin',
            name='manual_ordering',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
