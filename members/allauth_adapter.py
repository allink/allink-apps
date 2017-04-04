from allauth.account.adapter import DefaultAccountAdapter
from cms.models import Page


class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        # Redirects to the one page which has
        # the registered namespace "member" apphook
        # this site is used as a starting point to th member area
        try:
            return Page.objects.published().filter(application_namespace='members').order_by('-path')[0].get_absolute_url()
        except IndexError:
            raise IndexError('Apphook for members area is not defined. Please hook it to the desired page.')
