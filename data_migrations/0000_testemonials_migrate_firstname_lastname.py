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
        t.firstname = translation.old_firstname
        t.lastname = translation.old_lastname
        t.save(update_fields=['firstname', 'lastname'])


def _get_translation(object, TestimonialTranslation):
    translations = TestimonialTranslation.objects.filter(master_id=object.pk)
    try:
        return translations.get(language_code='de')
    except TestimonialTranslation.ObjectDoesNotExist:
        return translations.get()


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '__latest__'),
    ]

    operations = [
        migrations.RunPython(make_not_translated),
    ]
