# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170110_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogappcontentplugin',
            name='extra_css_classes',
            field=models.CharField(help_text='Only use this field if you know what your doing:<br>SPACE separated class names. Only valid CSS class names will work.', max_length=255, null=True, verbose_name='Additional CSS Classes for content-section', blank=True),
        ),
    ]
