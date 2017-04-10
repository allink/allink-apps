# -*- coding: utf-8 -*-
from allink_apps.config.models import Config


def config(request):
    config = Config.get_solo()
    return {'config': config}
