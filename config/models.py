# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from cms.models.fields import PageField

from solo.models import SingletonModel


@python_2_unicode_compatible
class Config(SingletonModel):

    architonic_user_id = models.IntegerField(
        verbose_name=_(u'Architonic User ID'),
        default=0
    )
    architonic_catalog_page = PageField(
        verbose_name=_(u'Architonic Katalog Seite'),
        null=True,
        on_delete=models.SET_NULL,
        help_text=_(u'Seite auf der sich das iframe zum Architonic Katalog befindet.')
    )

    def __str__(self):
        return u'Configuration'

    class Meta:
        verbose_name = _(u'Configuration')
