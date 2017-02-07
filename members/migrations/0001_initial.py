# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import parler.models
import aldryn_translation_tools.models
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('member_nr', models.CharField(unique=True, max_length=30, verbose_name='Member Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('first_name', models.CharField(max_length=255, null=True, verbose_name='Firstname', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='Lastname', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Members',
                'verbose_name_plural': 'Members',
            },
            bases=(aldryn_translation_tools.models.TranslationHelperMixin, aldryn_translation_tools.models.TranslatedAutoSlugifyMixin, parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MembersLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('log', models.CharField(max_length=255, verbose_name='Log')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('members', models.ForeignKey(to='members.Members')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='MembersTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('slug', models.SlugField(default=b'', max_length=255, blank=True, help_text='Leave blank to auto-generate a unique slug.', verbose_name='Slug')),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='members.Members', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'members_members_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'Members Translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='memberstranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
