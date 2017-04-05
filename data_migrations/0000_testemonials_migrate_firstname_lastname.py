# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import activate

from django.db import migrations, models

from allink_apps.testimonials.models import Testimonial


def make_not_translated(apps, schema_editor):
    TestimonialTranslation = apps.get_model('testimonials', 'TestimonialTranslation')
    TestimonialTranslation.language_code = 'de'
    activate('de')

    for t in Testimonial.objects.all():
        translation = _get_translation(t, TestimonialTranslation)
        t.firstname = translation.firstname
        t.lastname = translation.lastname
        t.save(update_fields=['firstname', 'lastname'])


def _get_translation(object, PeopleTranslation):
    translations = PeopleTranslation.objects.filter(master_id=object.pk)
    try:
        return translations.get(language_code='de')
    except PeopleTranslation.ObjectDoesNotExist:
        return translations.get()


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0016_auto_20170403_0409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonialtranslation',
            old_name='firstname',
            new_name='old_firstname',
        ),
        migrations.RenameField(
            model_name='testimonialtranslation',
            old_name='lastname',
            new_name='old_lastname',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='firstname',
            field=models.CharField(default=b'', max_length=255, verbose_name='Firstname'),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='lastname',
            field=models.CharField(default=b'', max_length=255, verbose_name='Lastname'),
        ),
        migrations.RunPython(make_not_translated),
    ]
