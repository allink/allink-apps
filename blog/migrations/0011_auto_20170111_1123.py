# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_teachers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teachers',
            options={'ordering': ('sort_order',)},
        ),
        migrations.AddField(
            model_name='teachers',
            name='sort_order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
        ),
    ]
