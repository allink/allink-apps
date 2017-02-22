# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import cms.models.fields
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('allink_categories', '0010_auto_20161209_0311'),
        ('allink_terms', '0002_auto_20170220_0725'),
        ('blog', '0006_auto_20170217_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventsregistration',
            name='end',
        ),
        migrations.RemoveField(
            model_name='eventsregistration',
            name='start',
        ),
        migrations.AddField(
            model_name='blog',
            name='content_placeholder',
            field=cms.models.fields.PlaceholderField(related_name='content_placeholder', slotname='blog_content', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='header_placeholder',
            field=cms.models.fields.PlaceholderField(related_name='header_placeholder', slotname='blog_header', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AddField(
            model_name='blogappcontentplugin',
            name='category_navigation_categories',
            field=models.ManyToManyField(help_text='You can explicitly define the categories for the category navigation here. This will override the automatically set of categories. (Either from "Filter & Ordering" or from the "Manual entries")', related_name='blog_blogappcontentplugin_category_navigation', verbose_name='Categories for Navigation', to='allink_categories.AllinkCategory', blank=True),
        ),
        migrations.AddField(
            model_name='eventsregistration',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
        ),
        migrations.AddField(
            model_name='eventsregistration',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
        ),
        migrations.AddField(
            model_name='eventsregistration',
            name='terms',
            field=models.ForeignKey(default=1, verbose_name='Terms', to='allink_terms.AllinkTerms'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventsregistration',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='eventsregistration',
            name='job',
            field=models.TextField(verbose_name='Education/ Job'),
        ),
        migrations.AlterField(
            model_name='eventsregistration',
            name='message',
            field=models.TextField(max_length=255, verbose_name='Message'),
        ),
    ]
