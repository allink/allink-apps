# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, FormView
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse
from django.template.loader import render_to_string
try:
    from django.contrib.sites.shortcuts import get_current_site
except ImportError:
    from django.contrib.sites.models import get_current_site

from .forms import MemberProfileEditForm
from .email import send_member_modified_email


class MembersIndex(TemplateView):
    template_name = 'members/index.html'


class MembersProfileEdit(FormView):
    form_class = MemberProfileEditForm
    template_name = "members/profile_edit.html"
    success_url = 'members'

    def get_initial(self):
        return {
            'email': self.request.user.email,
        }

    def form_valid(self, form):
        member = self.request.user.members
        member.email = form.cleaned_data.get('email')
        member.save()

        user = self.request.user
        user.email = form.cleaned_data.get('email')
        user.save()

        if 'email' in form.changed_data:
            member.log('email_changed_member', u'Email-Address changed in member-area.')

        if 'first_name' in form.changed_data:
            member.log('first_name_changed_member', u'Firstname changed in member-area.')

        if 'last_name' in form.changed_data:
            member.log('lastname_name_changed_member', u'Lastname changed in member-area.')

        # update mailchimp list
        member.put_to_mailchimp_list(form.initial.get('email'))

        # send notification email to staff
        send_member_modified_email(member)

        return JsonResponse({}, status=200)

    def form_invalid(self, form):
        return JsonResponse({
            'html': render_to_string(
                self.get_template_names(),
                self.get_context_data(form=form),
                request=self.request)
        }, status=400)
