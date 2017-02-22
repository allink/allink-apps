# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import allink_core.allink_base.models.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0003_auto_20170125_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='place',
            field=models.CharField(max_length=255, null=True, verbose_name='Place', blank=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='street',
            field=models.CharField(max_length=255, null=True, verbose_name='Street', blank=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='zip_code',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Zip Code', validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AlterField(
            model_name='testimonialappcontentplugin',
            name='manual_ordering',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
