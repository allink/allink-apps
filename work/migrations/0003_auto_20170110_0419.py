# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20161231_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workappcontentplugin',
            name='template',
            field=models.CharField(default=(b'grid_static', b'Grid (Static)'), help_text='Choose a template.', max_length=50, verbose_name='Template'),
        ),
    ]
