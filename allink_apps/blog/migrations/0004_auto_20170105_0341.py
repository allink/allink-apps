# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170103_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('blog_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='blog.Blog')),
                ('duration', models.CharField(help_text='Duration', max_length=255, null=True, blank=True)),
                ('teacher', models.CharField(help_text='Teacher', max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Courses/ Workshops',
                'verbose_name_plural': 'Courses/ Workshops',
            },
            bases=('blog.blog',),
        ),
        migrations.CreateModel(
            name='CoursesTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('costs', models.CharField(help_text='Costs', max_length=255, null=True, blank=True)),
                ('master', models.ForeignKey(related_name='translations_events', editable=False, to='blog.Courses', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'blog_courses_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'Courses/ Workshops Translation',
            },
        ),
        migrations.AlterField(
            model_name='events',
            name='event_time',
            field=models.CharField(help_text='Event Time', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eventstranslation',
            name='costs',
            field=models.CharField(help_text='Costs', max_length=255, null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='coursestranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
