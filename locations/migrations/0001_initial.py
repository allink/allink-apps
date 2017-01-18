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
import phonenumber_field.modelfields
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0006_auto_20160623_1627'),
        ('allink_categories', '0010_auto_20161209_0311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, verbose_name='Phone', blank=True)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, verbose_name='Mobile', blank=True)),
                ('fax', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, verbose_name='Fax', blank=True)),
                ('email', models.EmailField(default=b'', max_length=254, verbose_name='Email', blank=True)),
                ('website', models.URLField(null=True, verbose_name='Website', blank=True)),
                ('lat', models.FloatField(null=True, verbose_name='Latitude', blank=True)),
                ('lng', models.FloatField(null=True, verbose_name='Longitude', blank=True)),
                ('categories', models.ManyToManyField(to='allink_categories.AllinkCategory', blank=True)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
            bases=(aldryn_translation_tools.models.TranslationHelperMixin, aldryn_translation_tools.models.TranslatedAutoSlugifyMixin, parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='LocationsAppContentPlugin',
            fields=[
                ('title', models.CharField(help_text='The section title', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('title_size', models.CharField(default=b'h1', max_length=50, verbose_name='Section Title Size', choices=[(b'h1', 'Title Large'), (b'h2', 'Title Medium')])),
                ('container_enabled', models.BooleanField(default=True, help_text='If checked, an inner container with a maximum width is added', verbose_name='Activate "container"')),
                ('bg_color', models.IntegerField(blank=True, null=True, verbose_name='Set a predefined background color', choices=[(0, b'project-color-1'), (1, b'project-color-2'), (2, b'project-color-3')])),
                ('extra_css_classes', models.CharField(help_text='Comma separated class names. Only letters, numbers, hyphen and underscores are allowed in class names.', max_length=255, null=True, verbose_name='CSS Classes', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='locations_locationsappcontentplugin', primary_key=True, serialize=False, to='cms.CMSPlugin')),
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
                ('manual_entries', aldryn_common.admin_fields.sortedm2m.SortedM2MModelField(help_text='Select and arrange specific entries, or, leave blank to select all. (If manual entries are selected the category filtering will be ignored.)', to='locations.Locations', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(allink_core.allink_base.models.mixins.AllinkManualEntriesMixin, 'cms.cmsplugin'),
        ),
        migrations.CreateModel(
            name='LocationsImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
                ('image', filer.fields.image.FilerImageField(default=None, to='filer.Image', null=True)),
                ('location', adminsortable.fields.SortableForeignKey(blank=True, to='locations.Locations', help_text='The first image will be used as preview image.', null=True, verbose_name='Images')),
            ],
            options={
                'ordering': ('sort_order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocationsTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=255)),
                ('text', djangocms_text_ckeditor.fields.HTMLField(null=True, verbose_name='Text', blank=True)),
                ('zip', models.CharField(max_length=4, null=True, verbose_name='ZIP Code', blank=True)),
                ('city', models.CharField(max_length=127, null=True, verbose_name='City', blank=True)),
                ('street', models.CharField(max_length=255, null=True, verbose_name='City', blank=True)),
                ('slug', models.SlugField(default=b'', max_length=255, blank=True, help_text='Leave blank to auto-generate a unique slug.', verbose_name='Slug')),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='locations.Locations', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'locations_locations_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'Location Translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='locationstranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
