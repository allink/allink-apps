# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('allink_categories', '0010_auto_20161209_0311'),
        ('work', '0005_workappcontentplugin_category_navigation_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name': 'Software Produkt', 'verbose_name_plural': 'Software Produkte'},
        ),
        migrations.AlterModelOptions(
            name='worktranslation',
            options={'default_permissions': (), 'verbose_name': 'Software Produkt Translation', 'managed': True},
        ),
        migrations.RemoveField(
            model_name='workappcontentplugin',
            name='category_navigation_categories',
        ),
        migrations.AddField(
            model_name='work',
            name='content_placeholder',
            field=cms.models.fields.PlaceholderField(related_name='work_work_content_placeholder', slotname='work_content', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='header_placeholder',
            field=cms.models.fields.PlaceholderField(related_name='work_work_header_placeholder', slotname='work_header', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AddField(
            model_name='workappcontentplugin',
            name='category_navigation',
            field=models.ManyToManyField(help_text='You can explicitly define the categories for the category navigation here. This will override the automatically set of categories. (Either the one generated from "Filter & Ordering" or "Manual entries")', related_name='work_workappcontentplugin_category_navigation', verbose_name='Categories for Navigation', to='allink_categories.AllinkCategory', blank=True),
        ),
        migrations.AddField(
            model_name='workappcontentplugin',
            name='filter_fields',
            field=django.contrib.postgres.fields.ArrayField(help_text='For each choice a Select Dropdown will be displayed.', base_field=models.CharField(max_length=50, choices=[(b'categories', 'Categories')]), blank=True, default=None, null=True, size=None),
        ),
    ]
