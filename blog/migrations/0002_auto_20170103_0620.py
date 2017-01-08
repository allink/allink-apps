# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='eventstranslation',
            options={'default_permissions': (), 'verbose_name': 'Event Translation', 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News entry', 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='blog',
            name='end',
            field=models.DateTimeField(null=True, verbose_name='end', blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='start',
            field=models.DateTimeField(null=True, verbose_name='start', blank=True),
        ),
        migrations.AlterField(
            model_name='blogappcontentplugin',
            name='bg_color',
            field=models.IntegerField(blank=True, null=True, verbose_name='Set a predefined background color', choices=[(0, b'project-color-1'), (1, b'project-color-2'), (2, b'project-color-3')]),
        ),
    ]
