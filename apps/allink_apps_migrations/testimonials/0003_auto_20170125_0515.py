# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_auto_20170125_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='place',
            field=models.CharField(max_length=255, null=True, verbose_name='Place', blank=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='street',
            field=models.CharField(max_length=255, null=True, verbose_name='Street', blank=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Zipcode', validators=[django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AddField(
            model_name='testimonialappcontentplugin',
            name='detail_link_enabled',
            field=models.BooleanField(default=True, help_text='If checked, a link/button to the detail view will be displayed.', verbose_name='Show detail link'),
        ),
        migrations.AlterField(
            model_name='testimonialappcontentplugin',
            name='bg_image_outer_container',
            field=filer.fields.image.FilerImageField(related_name='testimonials_testimonialappcontentplugin_bg_image', blank=True, to='filer.Image', help_text='Optional: Set a background image for the content section.<br>Note: This is meant for decorative purposes only and should be used with care.', null=True, verbose_name='Background-Image'),
        ),
    ]
