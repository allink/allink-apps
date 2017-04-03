# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactrequest',
            name='contact_type',
            field=models.IntegerField(default=None, verbose_name='Please contact me via', choices=[(10, 'Phone'), (20, 'Courriel')]),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='cr\xe9\xe9', editable=False),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Courriel'),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps', choices=[(1, '08:00-10:00'), (2, '10:00-12:00'), (3, '12:00-14:00'), (4, '14:00-16:00'), (5, '16:00-18:00'), (6, '18:00-20:00')]),
        ),
    ]
