# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20170322_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrequest',
            name='street_additional',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Address Additional'),
        ),
    ]
