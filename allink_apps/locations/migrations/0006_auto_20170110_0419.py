# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0005_auto_20170109_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationsappcontentplugin',
            name='template',
            field=models.CharField(default=(b'grid_static', b'Grid (Static)'), help_text='Choose a template.', max_length=50, verbose_name='Template'),
        ),
    ]
