# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    Events = apps.get_model('blog', 'Events')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    new_ct = ContentType.objects.get_for_model(Events)
    Events.objects.filter(polymorphic_ctype__isnull=True).update(polymorphic_ctype=new_ct)

    News = apps.get_model('blog', 'News')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    new_ct = ContentType.objects.get_for_model(News)
    News.objects.filter(polymorphic_ctype__isnull=True).update(polymorphic_ctype=new_ct)

    Blog = apps.get_model('blog', 'Blog')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    new_ct = ContentType.objects.get_for_model(Blog)
    Blog.objects.filter(polymorphic_ctype__isnull=True).update(polymorphic_ctype=new_ct)


def backwards_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('blog', '0008_auto_20170306_0416'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]
