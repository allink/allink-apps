# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_members_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='email',
            field=models.EmailField(unique=True, max_length=254, verbose_name='Email'),
        ),
    ]
