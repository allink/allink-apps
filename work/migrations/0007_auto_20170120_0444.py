# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import allink_core.allink_base.models.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('work', '0006_auto_20170112_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='workappcontentplugin',
            name='bg_image_outer_container',
            field=filer.fields.image.FilerImageField(related_name='work_workappcontentplugin_bg_image', blank=True, to='filer.Image', help_text='Dimensions TBD', null=True, verbose_name='Background-Image'),
        ),
        migrations.AlterField(
            model_name='workappcontentplugin',
            name='bg_color',
            field=models.IntegerField(null=True, verbose_name='Set a predefined background color', blank=True),
        ),
        migrations.AlterField(
            model_name='workappcontentplugin',
            name='extra_css_classes',
            field=allink_core.allink_base.models.model_fields.Classes(default=b'', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Css Classes', blank=True),
        ),
    ]
