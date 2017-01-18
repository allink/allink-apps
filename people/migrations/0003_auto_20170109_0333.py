# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20161231_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='fax',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Required Formats: +41 (0) 41 345 67 89 or +41 41 345 67 89', max_length=128, null=True, verbose_name='Fax', blank=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Required Formats: +41 (0) 41 345 67 89 or +41 41 345 67 89', max_length=128, null=True, verbose_name='Mobile', blank=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Required Formats: +41 (0) 41 345 67 89 or +41 41 345 67 89', max_length=128, null=True, verbose_name='Phone', blank=True),
        ),
    ]
