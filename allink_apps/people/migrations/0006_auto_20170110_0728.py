# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20170110_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='company_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Company Name', blank=True),
        ),
        migrations.AddField(
            model_name='people',
            name='place',
            field=models.CharField(max_length=255, null=True, verbose_name='Place', blank=True),
        ),
    ]
