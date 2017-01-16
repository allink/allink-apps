# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import model_utils.fields
import adminsortable.fields
import allink_core.allink_base.models.mixins
import parler.models
import aldryn_translation_tools.models
import aldryn_common.admin_fields.sortedm2m
import django.utils.timezone
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0006_auto_20160623_1627'),
        ('allink_categories', '0010_auto_20161209_0311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('start', models.DateTimeField(null=True, verbose_name='start', blank=True)),
                ('end', models.DateTimeField(null=True, verbose_name='end', blank=True)),
                ('og_title', models.CharField(help_text='Title when shared on Facebook.', max_length=255, null=True, verbose_name='og:title', blank=True)),
                ('og_description', models.CharField(help_text='Description when shared on Facebook.', max_length=255, null=True, verbose_name='og:description', blank=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Blog entry',
                'verbose_name_plural': 'Blog entries',
            },
            bases=(aldryn_translation_tools.models.TranslationHelperMixin, aldryn_translation_tools.models.TranslatedAutoSlugifyMixin, parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='BlogAppContentPlugin',
            fields=[
                ('title', models.CharField(help_text='The section title', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('title_size', models.CharField(default=b'h1', max_length=50, verbose_name='Section Title Size', choices=[(b'h1', 'Title Large'), (b'h2', 'Title Medium')])),
                ('container_enabled', models.BooleanField(default=True, help_text='If checked, an inner container with a maximum width is added', verbose_name='Activate "container"')),
                ('bg_color', models.IntegerField(null=True, verbose_name='Set a predefined background color', blank=True)),
                ('extra_css_classes', models.CharField(help_text='Only use this field if you know what your doing:<br>SPACE separated class names. Only valid CSS class names will work.', max_length=255, null=True, verbose_name='Additional CSS Classes for content-section', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='blog_blogappcontentplugin', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('manual_ordering', models.CharField(blank=True, max_length=50, null=True, choices=[(b'title_asc', b'A-Z (title)'), (b'title_desc', b'Z-A (title'), (b'latest', b'latest first'), (b'oldest', b'oldest first')])),
                ('template', models.CharField(default=(b'grid_static', b'Grid (Static)'), help_text='Choose a template.', max_length=50, verbose_name='Template')),
                ('category_navigation_enabled', models.BooleanField(default=False, help_text='If checked, a filter navigation with all selected categories is displayed.<br>Please note: A category is only displayed if it contains items.', verbose_name='Show category navigation')),
                ('category_navigation_all', models.BooleanField(default=False, help_text='If checked, a category "all" in filter navigation is displayed.', verbose_name='Show category "all"')),
                ('softpage_enabled', models.BooleanField(default=True, help_text='If checked, the detail view of an entry will be displayed in a "softpage". Otherwise the page will be reloaded)', verbose_name='Show detailed information in Softpage')),
                ('items_per_row', models.IntegerField(default=3, help_text='Only applied if a "Grid" template has been selected.', verbose_name='Grid items per row', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
                ('paginated_by', models.IntegerField(default=9, help_text='Set to 0 if all entries should be displayed on first page.', verbose_name='Max. entries per page')),
                ('pagination_type', models.CharField(default=(b'no', b'None'), max_length=50, verbose_name='Paggination Type', choices=[(b'no', b'None'), (b'load', b'Add "Load More"-Button')])),
                ('load_more_button_text', models.CharField(help_text='If left blank, a default text will be used.', max_length=255, null=True, verbose_name='Text for "Load More"-Button', blank=True)),
                ('detail_link_text', models.CharField(help_text='If left blank, a default text will be used.', max_length=255, null=True, verbose_name='Text for "Detail"-Link', blank=True)),
                ('categories', models.ManyToManyField(to='allink_categories.AllinkCategory', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(allink_core.allink_base.models.mixins.AllinkManualEntriesMixin, 'cms.cmsplugin'),
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
            ],
            options={
                'ordering': ('sort_order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(default=b'', max_length=255, blank=True, help_text='Leave blank to auto-generate a unique slug.', verbose_name='Slug')),
                ('lead', djangocms_text_ckeditor.fields.HTMLField(help_text='Teaser text that in some cases is used in the list view and/or in the detail view.', null=True, verbose_name='Lead Text', blank=True)),
                ('text', djangocms_text_ckeditor.fields.HTMLField(help_text='The full text in detail view.', null=True, verbose_name='Detailed Text', blank=True)),
            ],
            options={
                'managed': True,
                'db_table': 'blog_blog_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'Blog entry Translation',
            },
        ),
        migrations.CreateModel(
            name='EventsTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('costs', models.CharField(help_text='Costs', max_length=255, null=True, blank=True)),
            ],
            options={
                'managed': True,
                'db_table': 'blog_events_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'Event Translation',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('blog_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='blog.Blog')),
                ('event_date', models.DateField(null=True, verbose_name='Event Date', blank=True)),
                ('event_time', models.CharField(help_text='Event Time', max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=('blog.blog',),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('blog_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='blog.Blog')),
            ],
            options={
                'verbose_name': 'Sales',
                'verbose_name_plural': 'Sales',
            },
            bases=('blog.blog',),
        ),
        migrations.AddField(
            model_name='blogtranslation',
            name='master',
            field=models.ForeignKey(related_name='translations', editable=False, to='blog.Blog', null=True),
        ),
        migrations.AddField(
            model_name='blogimage',
            name='blog',
            field=adminsortable.fields.SortableForeignKey(blank=True, to='blog.Blog', help_text='The first image will be used as preview image.', null=True, verbose_name='Images'),
        ),
        migrations.AddField(
            model_name='blogimage',
            name='image',
            field=filer.fields.image.FilerImageField(default=None, to='filer.Image', null=True),
        ),
        migrations.AddField(
            model_name='blogappcontentplugin',
            name='manual_entries',
            field=aldryn_common.admin_fields.sortedm2m.SortedM2MModelField(help_text='Select and arrange specific entries, or, leave blank to select all. (If manual entries are selected the category filtering will be ignored.)', to='blog.Blog', blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(to='allink_categories.AllinkCategory', blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='og_image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='Preview image when page/post is shared on Facebook. <br>Min. 1200 x 630 for best results.', null=True, verbose_name='og:Image'),
        ),
        migrations.AddField(
            model_name='eventstranslation',
            name='master',
            field=models.ForeignKey(related_name='translations_events', editable=False, to='blog.Events', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='blogtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='eventstranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
