# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.translation import activate

from allink_apps.people.models import People


def make_not_translated(apps, schema_editor):
    PeopleTranslation = apps.get_model('people', 'PeopleTranslation')
    PeopleTranslation.language_code = 'de'
    activate('de')

    for p in People.objects.all():
        translation = _get_translation(p, PeopleTranslation)
        p.firstname = translation.old_firstname
        p.lastname = translation.old_lastname
        p.save(update_fields=['firstname', 'lastname'])


def _get_translation(object, PeopleTranslation):
    translations = PeopleTranslation.objects.filter(master_id=object.pk)
    try:
        return translations.get(language_code='de')
    except PeopleTranslation.ObjectDoesNotExist:
        return translations.get()


class Migration(migrations.Migration):

    dependencies = [
        ('people', 'latest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peopletranslation',
            old_name='firstname',
            new_name='new_firstname',
        ),
        migrations.RenameField(
            model_name='peopletranslation',
            old_name='lastname',
            new_name='new_lastname',
        ),
        migrations.AddField(
            model_name='people',
            name='firstname',
            field=models.CharField(default=b'', max_length=255, verbose_name='Firstname'),
        ),
        migrations.AddField(
            model_name='people',
            name='lastname',
            field=models.CharField(default=b'', max_length=255, verbose_name='Lastname'),
        ),
        migrations.RunPython(make_not_translated),
    ]
