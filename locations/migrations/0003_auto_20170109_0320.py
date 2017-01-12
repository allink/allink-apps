# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20170105_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationstranslation',
            name='email',
            field=models.EmailField(default=b'', max_length=254, verbose_name='Email', blank=True),
        ),
        migrations.AddField(
            model_name='locationstranslation',
            name='fax',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, verbose_name='Fax', blank=True),
        ),
        migrations.AddField(
            model_name='locationstranslation',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, verbose_name='Mobile', blank=True),
        ),
        migrations.AddField(
            model_name='locationstranslation',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, verbose_name='Phone', blank=True),
        ),
        migrations.AlterField(
            model_name='locationstranslation',
            name='street',
            field=models.CharField(max_length=255, null=True, verbose_name='Street', blank=True),
        ),
    ]
