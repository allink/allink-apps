# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0010_auto_20170111_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='og_image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='Preview image when page/post is shared on Facebook. <br>Min. 1200 x 630 for best results.', null=True, verbose_name='og:Image'),
        ),
    ]
