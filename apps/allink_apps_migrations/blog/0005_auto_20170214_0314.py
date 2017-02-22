# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import allink_core.allink_base.models.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_events_event_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsRegistration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(null=True, verbose_name='start', blank=True)),
                ('end', models.DateTimeField(null=True, verbose_name='end', blank=True)),
                ('first_name', models.CharField(max_length=255, null=True, verbose_name='First Name', blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, verbose_name='Last Name', blank=True)),
                ('email', models.CharField(max_length=255, null=True, verbose_name='E-Mail-Adresse', blank=True)),
                ('street', models.CharField(max_length=255, null=True, verbose_name='Street', blank=True)),
                ('zip_code', models.PositiveIntegerField(blank=True, null=True, verbose_name='Zip Code', validators=[django.core.validators.MaxValueValidator(9999)])),
                ('place', models.CharField(max_length=255, null=True, verbose_name='Place', blank=True)),
                ('message', models.CharField(max_length=255, null=True, verbose_name='Message', blank=True)),
                ('job', models.TextField(null=True, verbose_name='Education/ Job', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='events',
            name='form_enabled',
            field=models.BooleanField(default=True, verbose_name='Event Form enabled'),
        ),
        migrations.AlterField(
            model_name='blogappcontentplugin',
            name='manual_ordering',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='eventsregistration',
            name='event',
            field=models.ForeignKey(to='blog.Events'),
        ),
    ]
