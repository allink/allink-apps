# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogappcontentplugin',
            name='bg_color',
            field=models.IntegerField(blank=True, null=True, verbose_name='Set a predefined background color', choices=[(0, b'project-color-1'), (1, b'project-color-2'), (2, b'project-color-3')]),
        ),
    ]
