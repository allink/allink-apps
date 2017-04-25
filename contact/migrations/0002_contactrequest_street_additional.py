# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrequest',
            name='street_additional',
            field=models.CharField(verbose_name='Address Additional', null=True, max_length=255, blank=True),
        ),
    ]
