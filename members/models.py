# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from parler.models import TranslatableModel, TranslatedFields
from model_utils.models import TimeStampedModel
from aldryn_translation_tools.models import (
    TranslatedAutoSlugifyMixin,
    TranslationHelperMixin,
)
from .utils import update_mailchimp_list_member

@python_2_unicode_compatible
class Members(TranslationHelperMixin, TranslatedAutoSlugifyMixin, TranslatableModel, TimeStampedModel):
    slug_source_field_name = 'full_name'

    translations = TranslatedFields(
        slug=models.SlugField(
            _(u'Slug'),
            max_length=255,
            default='',
            blank=True,
            help_text=_(u'Leave blank to auto-generate a unique slug.')
        )
    )

    member_nr = models.CharField(
        _(u'Member Number'),
        max_length=30,
        unique=True,
        blank=False
    )

    email = models.EmailField(
        _(u'Email'),
        unique=True,
    )

    first_name = models.CharField(
        _(u'Firstname'),
        max_length=255,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        _(u'Lastname'),
        max_length=30,
        blank=True
    )

    language = models.CharField(
        _(u'Language'),
        max_length=3,
        default=settings.LANGUAGE_CODE
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        app_label = 'members'
        verbose_name = _('Members')
        verbose_name_plural = _('Members')

    def __str__(self):
        return '{}: {} {}'.format(self.member_nr, self.user.first_name, self.user.last_name)

    @property
    def full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def save(self, **kwargs):
        if not self.pk:
            user = User.objects.create_user(
                username=self.member_nr,
                email=self.email,
                password=settings.MEMBERS_INITIAL_PWD,
                first_name=self.first_name,
                last_name=self.last_name
            )
            group = Group.objects.get_or_create(name='Member')
            user.groups.add(group[0])
            self.user = user
            update_mailchimp_list_member(self)
        else:
            self.user.username = self.member_nr
            self.user.email = self.email
            self.user.last_name = self.last_name
            self.user.first_name = self.first_name
            self.user.save()
        super(Members, self).save(**kwargs)


    def delete(self, *args, **kwargs):
        if self.user:
            self.user.delete()
        super(Members, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        app = '{}:detail'.format(self._meta.model_name)
        return reverse(app, kwargs={'slug': self.slug})

    def log(self, log, description):
        MembersLog.objects.create(members=self, log=log, description=description)


@python_2_unicode_compatible
class MembersLog(models.Model):
    log = models.CharField(
        _(u'Log'),
        max_length=255
    )

    description = models.CharField(
        _(u'Description'),
        max_length=255
    )

    members = models.ForeignKey(Members)

    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.log

