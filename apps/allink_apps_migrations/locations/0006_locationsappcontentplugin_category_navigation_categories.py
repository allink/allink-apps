# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allink_categories', '0010_auto_20161209_0311'),
        ('locations', '0005_locations_street_nr'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationsappcontentplugin',
            name='category_navigation_categories',
            field=models.ManyToManyField(help_text='You can explicitly define the categories for the category navigation here. This will override the automatically set of categories. (Either from "Filter & Ordering" or from the "Manual entries")', related_name='locations_locationsappcontentplugin_category_navigation', verbose_name='Categories for Navigation', to='allink_categories.AllinkCategory', blank=True),
        ),
    ]