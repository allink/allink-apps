# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from allink_core.allink_base.models import AllinkSimpleRegistrationFieldsModel
from allink_core.allink_base.models.choices import SALUTATION_CHOICES


class ContactRequestBase(AllinkSimpleRegistrationFieldsModel):

    TIME_CHOICES = (
        (None, _(u'-- between --')),
        (1, u'09:00-11:00'),
        (2, u'13:00-15:00'),
        (3, u'15:00-17:00'),
    )
    CONTACT_PHONE = 10
    CONTACT_EMAIL = 20

    CONTACT_CHOICES = (
        (None, _(u'-- please choose --')),
        (CONTACT_PHONE, _(u'Phone')),
        (CONTACT_EMAIL, _(u'E-Mail')),
    )
    salutation = models.IntegerField(
        _(u'Salutation'),
        choices=SALUTATION_CHOICES,
        null=True
    )
    company_name = models.CharField(
        _(u'Company'),
        max_length=255,
        blank=True,
        null=True
    )
    contact_type = models.IntegerField(
        _(u'Please contact me via'),
        choices=CONTACT_CHOICES,
    )
    phone = models.CharField(
        _(u'Phone'),
        max_length=30,
        blank=True,
        null=True
    )
    date = models.DateField(
        _(u'Date'),
        blank=True,
        null=True
    )
    time = models.IntegerField(
        _(u'Time'),
        choices=TIME_CHOICES,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    @property
    def contact_details(self):
        """
        Returns either the email address or the telephone number, depending on contact_type field
        """
        return self.phone if self.contact_type == self.CONTACT_PHONE else self.email

    @classmethod
    def get_verbose_name(cls):
        from allink_core.allink_config.models import AllinkConfig
        try:
            field_name = cls._meta.model_name + '_verbose'
            return getattr(AllinkConfig.get_solo(), field_name)
        except AttributeError:
            return cls._meta.verbose_name

    @classmethod
    def get_verbose_name_plural(cls):
        from allink_core.allink_config.models import AllinkConfig
        try:
            field_name = cls._meta.model_name + '_verbose_plural'
            return getattr(AllinkConfig.get_solo(), field_name)
        except AttributeError:
            return cls._meta.verbose_name_plural


class ContactRequest(ContactRequestBase):

    class Meta:
        verbose_name = _(u'Contact Request')
        verbose_name_plural = _(u'Contact Requests')
