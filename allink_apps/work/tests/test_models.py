# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TransactionTestCase
from django.utils.translation import override, force_text

from ..models import Work

from . import (
    DefaultSetupMixin, DefaultApphookMixin, CleanUpMixin, BaseWorkTest,
)


class TestBasicWorkModels(DefaultSetupMixin,
                            DefaultApphookMixin,
                            CleanUpMixin,
                            TransactionTestCase):

    def setUp(self):
        super(TestBasicWorkModels, self).setUp()
        # get some time to reload urls
        self.client.get(self.app_hook_page.get_absolute_url())

    def test_create_work(self):
        """We can create a work with a title."""
        title = 'Work Test 1'
        work = Work.objects.create(title=title)
        self.assertEqual(work.title, title)
        self.assertEqual(Work.objects.all()[0], work)

    def test_delete_work(self):
        """We can delete a work."""
        title = 'Work Delete'
        work = Work.objects.create(title=title)
        Work.objects.get(pk=work.pk).delete()
        self.assertFalse(Work.objects.filter(pk=work.pk))

    def test_str(self):
        title = 'Work Str'
        work = Work.objects.create(title=title)
        self.assertEqual(force_text(work), title)

    def test_absolute_url(self):
        slug = 'work-slug'
        work = Work.objects.create(slug=slug)
        # This isn't a translation test, per se, but let's make sure that we
        # have a predictable language prefix, regardless of the tester's locale.
        with override('en'):
            app_hook_url = self.app_hook_page.get_absolute_url()
            self.assertEqual(
                work.get_absolute_url(),
                '{0}{1}/'.format(app_hook_url, slug)
            )
            # Now test that it will work when there's no slug too.
            work.slug = ''
            self.assertEqual(
                work.get_absolute_url(),
                '{0}{1}/'.format(app_hook_url, work.pk),
            )

    def test_auto_slugify(self):
        title = 'Project Test with Hans'
        slug = 'project-test-with-hans'
        work = Work.objects.create(title=title)
        work.save()
        self.assertEquals(work.slug, slug)

    def test_auto_slugify_same_title(self):
        title_1 = 'Project Test with Hans'
        slug_1 = 'project-test-with-hans'
        work_1 = Work.objects.create(title=title_1)
        work_1.save()

        title_2 = 'Project Test with Hans'
        slug_2 = 'project-test-with-hans-1'
        work_2 = Work.objects.create(title=title_2)
        work_2.save()

        self.assertEquals(work_1.slug, slug_1)
        self.assertEquals(work_2.slug, slug_2)


class TestWorkModelTranslation(BaseWorkTest):

    def test_work_translatable(self):
        work1 = self.reload(self.work1, 'en')
        self.assertEqual(
            work1.title,
            self.data['work1']['en']['title']
        )
        work1 = self.reload(self.work1, 'de')
        self.assertEqual(
            work1.safe_translation_getter('title'),
            self.data['work1']['de']['title']
        )

    def test_lead(self):
        work1 = self.reload(self.work1, 'en')
        self.assertEqual(
            work1.lead,
            self.data['work1']['en']['lead']
        )
        work1 = self.reload(self.work1, 'de')
        self.assertEqual(
            work1.lead,
            self.data['work1']['de']['lead']
        )
