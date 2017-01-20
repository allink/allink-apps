# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import allink_core.allink_base.models.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0006_auto_20170112_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonialappcontentplugin',
            name='extra_css_classes',
            field=allink_core.allink_base.models.model_fields.Classes(default=b'', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Css Classes', blank=True),
        ),
    ]
