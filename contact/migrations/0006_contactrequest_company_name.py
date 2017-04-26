# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_contactrequest_street_additional'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrequest',
            name='company_name',
            field=models.CharField(max_length=255, blank=True, verbose_name='Company', null=True),
        ),
    ]
