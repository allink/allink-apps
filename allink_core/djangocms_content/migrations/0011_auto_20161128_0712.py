# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_content', '0010_auto_20161128_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='overlay_styles_enabled',
            field=models.BooleanField(help_text='If checked, the predefined overlay styles are applied (suitable when text is over an image/video)', verbose_name='Activate overlay styles'),
        ),
    ]