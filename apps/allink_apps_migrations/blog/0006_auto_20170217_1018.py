# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170214_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsregistration',
            name='street_nr',
            field=models.CharField(max_length=50, null=True, verbose_name='Street Nr.', blank=True),
        ),
        migrations.AlterField(
            model_name='eventsregistration',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email', blank=True),
        ),
        migrations.AlterField(
            model_name='eventsregistration',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='eventsregistration',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='eventsregistration',
            name='message',
            field=models.CharField(max_length=255, verbose_name='Message'),
        ),
    ]
