# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0009_locations_zoom_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locations',
            name='zoom_level',
        ),
        migrations.AddField(
            model_name='locationsappcontentplugin',
            name='zoom_level',
            field=models.IntegerField(default=14, help_text='The higher the number, the more we zoom in.', verbose_name='Zoom Level', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)]),
        ),
    ]
