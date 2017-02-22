# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20170125_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='street',
            field=models.CharField(max_length=255, null=True, verbose_name='Street', blank=True),
        ),
        migrations.AddField(
            model_name='people',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Zipcode', validators=[django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AddField(
            model_name='peopleappcontentplugin',
            name='detail_link_enabled',
            field=models.BooleanField(default=True, help_text='If checked, a link/button to the detail view will be displayed.', verbose_name='Show detail link'),
        ),
        migrations.AlterField(
            model_name='peopleappcontentplugin',
            name='bg_image_outer_container',
            field=filer.fields.image.FilerImageField(related_name='people_peopleappcontentplugin_bg_image', blank=True, to='filer.Image', help_text='Optional: Set a background image for the content section.<br>Note: This is meant for decorative purposes only and should be used with care.', null=True, verbose_name='Background-Image'),
        ),
    ]
