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
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('categories', models.ManyToManyField(to='allink_categories.AllinkCategory', blank=True)),
            ],
            options={
                'verbose_name': 'Projekt/ Referenz',
                'verbose_name_plural': 'Projekte/ Referenzen',
            },
            bases=(aldryn_translation_tools.models.TranslationHelperMixin, aldryn_translation_tools.models.TranslatedAutoSlugifyMixin, parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='WorkAppContentPlugin',
            fields=[
                ('title', models.CharField(help_text='The section title', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('title_size', models.CharField(default=b'h1', max_length=50, verbose_name='Section Title Size', choices=[(b'h1', 'Title Large'), (b'h2', 'Title Medium')])),
                ('container_enabled', models.BooleanField(default=True, help_text='If checked, an inner container with a maximum width is added', verbose_name='Activate "container"')),
                ('bg_color', models.IntegerField(null=True, verbose_name='Set a predefined background color', blank=True)),
                ('extra_css_classes', models.CharField(help_text='Comma separated class names. Only letters, numbers, hyphen and underscores are allowed in class names.', max_length=255, null=True, verbose_name='CSS Classes', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='work_workappcontentplugin', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('manual_ordering', models.CharField(blank=True, max_length=50, null=True, choices=[(b'title_asc', b'A-Z (title)'), (b'title_desc', b'Z-A (title'), (b'latest', b'latest first'), (b'oldest', b'oldest first')])),
                ('template', models.CharField(default=(b'grid_dynamic', b'Grid (Dynamic)'), help_text='Choose a template.', max_length=50, verbose_name='Template')),
                ('category_navigation_enabled', models.BooleanField(default=False, help_text='If checked, a filter navigation with all selected categories is displayed.<br>Please note: A category is only displayed if it contains items.', verbose_name='Show category navigation')),
                ('category_navigation_all', models.BooleanField(default=False, help_text='If checked, a category "all" in filter navigation is displayed.', verbose_name='Show category "all"')),
                ('softpage_enabled', models.BooleanField(default=True, help_text='If checked, the detail view of an entry will be displayed in a "softpage". Otherwise the page will be reloaded)', verbose_name='Show detailed information in Softpage')),
                ('items_per_row', models.IntegerField(default=3, help_text='Only applied if a "Grid" template has been selected.', verbose_name='Grid items per row', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
                ('paginated_by', models.IntegerField(default=9, help_text='Set to 0 if all entries should be displayed on first page.', verbose_name='Max. entries per page')),
                ('pagination_type', models.CharField(default=(b'no', b'None'), max_length=50, verbose_name='Paggination Type', choices=[(b'no', b'None'), (b'load', b'Add "Load More"-Button')])),
                ('load_more_button_text', models.CharField(help_text='If left blank, a default text will be used.', max_length=255, null=True, verbose_name='Text for "Load More"-Button', blank=True)),
                ('detail_link_text', models.CharField(help_text='If left blank, a default text will be used.', max_length=255, null=True, verbose_name='Text for "Detail"-Link', blank=True)),
                ('categories', models.ManyToManyField(to='allink_categories.AllinkCategory', blank=True)),
                ('manual_entries', aldryn_common.admin_fields.sortedm2m.SortedM2MModelField(help_text='Select and arrange specific entries, or, leave blank to select all. (If manual entries are selected the category filtering will be ignored.)', to='work.Work', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(allink_core.allink_base.models.mixins.AllinkManualEntriesMixin, 'cms.cmsplugin'),
        ),
        migrations.CreateModel(
            name='WorkImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
                ('image', filer.fields.image.FilerImageField(default=None, to='filer.Image', null=True)),
                ('work', adminsortable.fields.SortableForeignKey(blank=True, to='work.Work', help_text='The first image will be used as preview image.', null=True, verbose_name='Images')),
            ],
            options={
                'ordering': ('sort_order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(default=b'', max_length=255, blank=True, help_text='Leave blank to auto-generate a unique slug.', verbose_name='Slug')),
                ('lead', djangocms_text_ckeditor.fields.HTMLField(help_text='Used as a teaser. Not displayed in detail view.', null=True, verbose_name='Lead Text', blank=True)),
                ('text', djangocms_text_ckeditor.fields.HTMLField(help_text='The full text in detail view.', null=True, verbose_name='Detailed Text', blank=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='work.Work', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'work_work_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'Projekt/ Referenz Translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='worktranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
