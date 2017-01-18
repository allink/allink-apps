# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20170109_0320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationstranslation',
            name='email',
        ),
        migrations.RemoveField(
            model_name='locationstranslation',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='locationstranslation',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='locationstranslation',
            name='phone',
        ),
    ]
