# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import allink_core.allink_base.models.model_fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('street', models.CharField(max_length=255, null=True, verbose_name='Street', blank=True)),
                ('street_nr', models.CharField(max_length=50, null=True, verbose_name='Street Nr.', blank=True)),
                ('zip_code', allink_core.allink_base.models.model_fields.ZipCodeField(null=True, verbose_name='Zip Code', blank=True)),
                ('place', models.CharField(max_length=255, null=True, verbose_name='Place', blank=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(max_length=255, null=True, verbose_name='Message', blank=True)),
                ('contact_type', models.IntegerField(default=None, verbose_name='Please contact me via', choices=[(10, 'Phone'), (20, 'Email')])),
                ('date', models.DateField(null=True, verbose_name='Date', blank=True)),
                ('time', models.IntegerField(blank=True, null=True, verbose_name='Time', choices=[(1, '08:00-10:00'), (2, '10:00-12:00'), (3, '12:00-14:00'), (4, '14:00-16:00'), (5, '16:00-18:00'), (6, '18:00-20:00')])),
            ],
            options={
                'verbose_name': 'Contact Request',
                'verbose_name_plural': 'Contact Requests',
            },
        ),
    ]
