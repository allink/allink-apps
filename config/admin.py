# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.utils.translation import ugettext_lazy as _

from solo.admin import SingletonModelAdmin

from allink_apps.config.models import Config

require_POST = method_decorator(require_POST)


@admin.register(Config)
class ConfigAdmin(SingletonModelAdmin):
    pass
