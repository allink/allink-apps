# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
def delete_plugins(apps, schema_editor):
    OldPlugin = apps.get_model("cms", "cmsplugin")

    for old in OldPlugin.objects.filter(plugin_type='CMSAllinkGalleryImagePlugin', placeholder_id=72):
        old.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_auto_20170306_0416'),
    ]

    operations = [
        migrations.RunPython(delete_plugins),
    ]
