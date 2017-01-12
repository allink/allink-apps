# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('locations', '0007_auto_20170110_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='og_description',
            field=models.CharField(help_text='Description when shared on Facebook.', max_length=255, null=True, verbose_name='og:description', blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='og_image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='Image when shared on Facebook.', null=True, verbose_name='og:Image'),
        ),
        migrations.AddField(
            model_name='locations',
            name='og_title',
            field=models.CharField(help_text='Title when shared on Facebook.', max_length=255, null=True, verbose_name='og:title', blank=True),
        ),
    ]
