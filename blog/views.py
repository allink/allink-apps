# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from allink_core.allink_base.views import AllinkBasePluginLoadMoreView, AllinkBaseDetailView, AllinkBaseCreateView
from allink_core.allink_mandrill.config import MandrillConfig
from allink_core.allink_terms.models import AllinkTerms

from .models import Blog, BlogAppContentPlugin, EventsRegistration, Events
from .forms import EventsRegistrationForm
from .email import send_registration_confirmation_email, send_registration_email

config = MandrillConfig()

class BlogPluginLoadMore(AllinkBasePluginLoadMoreView):
    model = Blog
    plugin_model = BlogAppContentPlugin


class BlogDetail(AllinkBaseDetailView):
    model = Blog

    def get_template_names(self):
        names = []
        if hasattr(self.object, 'events'):
            name = self.object.events._meta.model_name
        elif hasattr(self.object, 'news'):
            name = self.object.news._meta.model_name
        else:
            name = self.object._meta.model_name

        names.append("%s/%s%s.html" % (name, name, self.template_name_suffix))
        return names


class EventsRegistrationView(AllinkBaseCreateView):
    model = EventsRegistration
    form_class = EventsRegistrationForm
    template_name = 'events/forms/registration.html'

    def get_context_data(self, **kwargs):
        context = super(AllinkBaseCreateView, self).get_context_data(**kwargs)
        context.update({
            'slug': self.kwargs.get('slug', None)
        })
        return context

    def get_initial(self):
        self.item = Events.objects.get(translations__slug=self.kwargs.get('slug', None))
        initial = super(EventsRegistrationView, self).get_initial()
        initial = initial.copy()
        initial['event'] = self.item
        initial['terms'] = AllinkTerms.objects.get_published()
        return initial

    def form_valid(self, form):
        response = super(EventsRegistrationView, self).form_valid(form)
        self.send_mail()
        return response

    def send_mail(self):
        send_registration_email(self.get_form(), self.item)
        send_registration_confirmation_email(self.get_form(), self.item)
