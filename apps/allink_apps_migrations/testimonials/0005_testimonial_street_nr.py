# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0004_auto_20170214_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='street_nr',
            field=models.CharField(max_length=50, null=True, verbose_name='Street Nr.', blank=True),
        ),
    ]
