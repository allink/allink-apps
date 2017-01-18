# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import adminsortable.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_merge'),
        ('blog', '0009_remove_courses_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('external', models.CharField(help_text='Intern teacher will override this field.', max_length=255, null=True, verbose_name='External teacher', blank=True)),
                ('link', models.URLField(help_text='Only used when extern teacher is filled.', null=True, verbose_name='Link', blank=True)),
                ('courses', adminsortable.fields.SortableForeignKey(blank=True, to='blog.Courses', null=True)),
                ('intern', models.ForeignKey(verbose_name='Intern teacher', blank=True, to='people.People', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
