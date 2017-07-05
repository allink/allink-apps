# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import activate
from django.db import migrations, models
from django.conf import settings


def translate_meta_fields(apps, schema_editor):
    Blog = apps.get_model('blog', 'Blog')
    BlogTranslation = apps.get_model('blog', 'BlogTranslation')
    language_code = settings.LANGUAGES[0][0]
    activate(language_code)

    for b in Blog.objects.all():
        translation = _get_translation(b, BlogTranslation)
        translation.og_title = b.old_og_title
        translation.og_description = b.old_og_description
        translation.disable_base_title = b.old_disable_base_title
        translation.save(update_fields=['og_title', 'og_description', 'disable_base_title'])


def _get_translation(object, translation_class):
    translations = translation_class.objects.filter(master_id=object.pk)
    language_code = settings.LANGUAGES[0][0]
    try:
        return translations.get(language_code=language_code)
    except translation_class.DoesNotExist:
        try:
            return translations.get()
        except:
            object.create_translation(language_code, og_title='')
            return translations.get(language_code=language_code)


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20170629_1157'),
    ]

    operations = [
        migrations.RunPython(translate_meta_fields)
    ]
