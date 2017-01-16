# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0011_auto_20170112_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='fax',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Required Format: +41 41 345 67 89', max_length=128, null=True, verbose_name='Fax', blank=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Required Format: +41 41 345 67 89', max_length=128, null=True, verbose_name='Mobile', blank=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Required Format: +41 41 345 67 89', max_length=128, null=True, verbose_name='Phone', blank=True),
        ),
    ]
