# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
def delete_plugins(apps, schema_editor):
    OldPlugin = apps.get_model("cms", "cmsplugin")

    for old in OldPlugin.objects.filter(plugin_type__in=['CMSAllinkGalleryImagePlugin', 'CMSAllinkImagePlugin'],
                                        placeholder_id__in=[68, 69, 70, 71, 71, 73, 74]):
        old.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('work', '0007_auto_20170307_0154'),
    ]

    operations = [
        migrations.RunPython(delete_plugins),
    ]
