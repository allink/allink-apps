# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import allink_core.allink_base.models.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20170125_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationstranslation',
            name='city',
        ),
        migrations.RemoveField(
            model_name='locationstranslation',
            name='street',
        ),
        migrations.RemoveField(
            model_name='locationstranslation',
            name='zip',
        ),
        migrations.AddField(
            model_name='locations',
            name='fri',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm"', max_length=100, verbose_name='Friday morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='fri_afternoon',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', max_length=100, verbose_name='Friday mo morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='mon',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm"', max_length=100, verbose_name='Monday morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='mon_afternoon',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', max_length=100, verbose_name='Monday morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='place',
            field=models.CharField(max_length=255, null=True, verbose_name='Place', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='sat',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm"', max_length=100, verbose_name='Saturday morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='sat_afternoon',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', max_length=100, verbose_name='Saturday  morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='street',
            field=models.CharField(max_length=255, null=True, verbose_name='Street', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='sun',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm"', max_length=100, verbose_name='Sunday morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='sun_afternoon',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', max_length=100, verbose_name='Sunday mo morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='thu',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm"', max_length=100, verbose_name='Thursday morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='thu_afternoon',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', max_length=100, verbose_name='Thursday morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='tue',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm"', max_length=100, verbose_name='Tuesday morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='tue_afternoon',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', max_length=100, verbose_name='Tuesday morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='wed',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm"', max_length=100, verbose_name='Wednesday morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='wed_afternoon',
            field=models.CharField(help_text='Format: "(h)h:mm-(h)h:mm", only fill if location has a lunch break', max_length=100, verbose_name='Wednesday morning or whole day', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='zip_code',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Zip Code', validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AlterField(
            model_name='locations',
            name='lat',
            field=models.FloatField(null=True, verbose_name='Latitude', blank=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='lng',
            field=models.FloatField(null=True, verbose_name='Longitude', blank=True),
        ),
        migrations.AlterField(
            model_name='locationsappcontentplugin',
            name='manual_ordering',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
