# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('allink_categories', '0007_remove_allinkcategorytranslation_app_category_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='allinkcategory',
            name='app_category_label',
            field=django.contrib.postgres.fields.ArrayField(help_text='Please specify the app which uses this categories.', null=True, base_field=models.CharField(max_length=50), size=None, blank=True),
        ),
    ]
