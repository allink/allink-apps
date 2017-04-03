from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

from .models import Locations


class LocationsMenu(CMSAttachMenu):

    name = _("Locations menu")
    def get_nodes(self, request):

        nodes = []
        for entry in Locations.objects.active():
            node = NavigationNode(
                entry.title,
                entry.get_absolute_url(),
                entry.sort_order,
                attr={
                    'description': entry.lead
                })
            nodes.append(node)

        return nodes

menu_pool.register_menu(LocationsMenu)
