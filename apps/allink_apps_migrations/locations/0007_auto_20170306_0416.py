# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields
import allink_core.allink_base.models.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('allink_categories', '0010_auto_20161209_0311'),
        ('locations', '0006_locationsappcontentplugin_category_navigation_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationsappcontentplugin',
            name='category_navigation_categories',
        ),
        migrations.AddField(
            model_name='locationsappcontentplugin',
            name='category_navigation',
            field=models.ManyToManyField(help_text='You can explicitly define the categories for the category navigation here. This will override the automatically set of categories. (Either the one generated from "Filter & Ordering" or "Manual entries")', related_name='locations_locationsappcontentplugin_category_navigation', verbose_name='Categories for Navigation', to='allink_categories.AllinkCategory', blank=True),
        ),
        migrations.AddField(
            model_name='locationsappcontentplugin',
            name='filter_fields',
            field=django.contrib.postgres.fields.ArrayField(help_text='For each choice a Select Dropdown will be displayed.', base_field=models.CharField(max_length=50, choices=[(b'categories', 'Categories')]), blank=True, default=None, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='locations',
            name='zip_code',
            field=allink_core.allink_base.models.model_fields.ZipCodeField(null=True, verbose_name='Zip Code', blank=True),
        ),
    ]
