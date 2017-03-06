# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields
import allink_core.allink_base.models.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('allink_categories', '0010_auto_20161209_0311'),
        ('testimonials', '0006_testimonialappcontentplugin_category_navigation_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonial',
            options={'verbose_name': 'Unternehmen', 'verbose_name_plural': 'Unternehmen'},
        ),
        migrations.AlterModelOptions(
            name='testimonialtranslation',
            options={'default_permissions': (), 'verbose_name': 'Unternehmen Translation', 'managed': True},
        ),
        migrations.RemoveField(
            model_name='testimonialappcontentplugin',
            name='category_navigation_categories',
        ),
        migrations.AddField(
            model_name='testimonialappcontentplugin',
            name='category_navigation',
            field=models.ManyToManyField(help_text='You can explicitly define the categories for the category navigation here. This will override the automatically set of categories. (Either the one generated from "Filter & Ordering" or "Manual entries")', related_name='testimonials_testimonialappcontentplugin_category_navigation', verbose_name='Categories for Navigation', to='allink_categories.AllinkCategory', blank=True),
        ),
        migrations.AddField(
            model_name='testimonialappcontentplugin',
            name='filter_fields',
            field=django.contrib.postgres.fields.ArrayField(help_text='For each choice a Select Dropdown will be displayed.', base_field=models.CharField(max_length=50, choices=[(b'categories', 'Categories')]), blank=True, default=None, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='zip_code',
            field=allink_core.allink_base.models.model_fields.ZipCodeField(null=True, verbose_name='Zip Code', blank=True),
        ),
    ]
