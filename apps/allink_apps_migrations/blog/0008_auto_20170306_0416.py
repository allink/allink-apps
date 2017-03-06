# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields
import cms.models.fields
import allink_core.allink_base.models.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('allink_categories', '0010_auto_20161209_0311'),
        ('blog', '0007_auto_20170222_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogappcontentplugin',
            name='category_navigation_categories',
        ),
        migrations.AddField(
            model_name='blog',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_blog.blog_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='blogappcontentplugin',
            name='category_navigation',
            field=models.ManyToManyField(help_text='You can explicitly define the categories for the category navigation here. This will override the automatically set of categories. (Either the one generated from "Filter & Ordering" or "Manual entries")', related_name='blog_blogappcontentplugin_category_navigation', verbose_name='Categories for Navigation', to='allink_categories.AllinkCategory', blank=True),
        ),
        migrations.AddField(
            model_name='blogappcontentplugin',
            name='filter_fields',
            field=django.contrib.postgres.fields.ArrayField(help_text='For each choice a Select Dropdown will be displayed.', base_field=models.CharField(max_length=50, choices=[(b'categories', 'Categories')]), blank=True, default=None, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content_placeholder',
            field=cms.models.fields.PlaceholderField(related_name='blog_blog_content_placeholder', slotname='blog_content', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='header_placeholder',
            field=cms.models.fields.PlaceholderField(related_name='blog_blog_header_placeholder', slotname='blog_header', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AlterField(
            model_name='eventsregistration',
            name='message',
            field=models.TextField(max_length=255, null=True, verbose_name='Message', blank=True),
        ),
        migrations.AlterField(
            model_name='eventsregistration',
            name='terms',
            field=models.ForeignKey(verbose_name='I have read and accept the terms and conditions.', to='allink_terms.AllinkTerms', null=True),
        ),
        migrations.AlterField(
            model_name='eventsregistration',
            name='zip_code',
            field=allink_core.allink_base.models.model_fields.ZipCodeField(null=True, verbose_name='Zip Code', blank=True),
        ),
    ]
