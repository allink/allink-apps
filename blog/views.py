# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from allink_core.allink_base.views import AllinkBasePluginLoadMoreView, AllinkBaseDetailView, AllinkBaseAjaxFormView
from .models import Blog, BlogAppContentPlugin
from .forms import EventsRegistrationForm

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

        names.append("%s/%s%s.html" % (
            self.object._meta.app_label,
            name,
            self.template_name_suffix
        ))
        return names

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)

        if hasattr(self.object, 'events'):
            form = EventsRegistrationForm()
            context.update({
                'form': form
            })
        return context

    # def form_valid(self, form):
    #     if self.request.is_ajax():
    #         return JsonResponse({}, status=200)
    #     else:
    #         return super(BlogDetail, self).form_valid()
    #
    #
    #
    # def form_invalid(self, form):
    #     return JsonResponse({
    #         'html': render_to_string(
    #             self.get_template_names(),
    #             self.get_context_data(form=form),
    #             request=self.request)
    #     }, status=400)



class EventRegister(AllinkBaseAjaxFormView):
    form_class = EventsRegistrationForm
    template_name = 'blog/events_register_detail.html'
    # template_name = 'blog/events_detail.html'
    success_url = '/'

    # def get_context_data(self, **kwargs):
    #     super(EventsRegistrationForm, )
