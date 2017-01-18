# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170111_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachers',
            old_name='intern',
            new_name='internal',
        ),
        migrations.RenameField(
            model_name='teachers',
            old_name='link',
            new_name='website',
        ),
        migrations.AlterField(
            model_name='blog',
            name='og_image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='Preview image when page/post is shared on Facebook. <br>Min. 1200 x 630 for best results.', null=True, verbose_name='og:Image'),
        ),
    ]
