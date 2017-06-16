# -*- coding: utf-8 -*-
import datetime
from django.http import HttpResponse

from allink_core.allink_base.views import AllinkBasePluginLoadMoreView, AllinkBaseDetailView
from allink_apps.work.models import Work, WorkAppContentPlugin
from .pdf import PdfWork

class WorkPluginLoadMore(AllinkBasePluginLoadMoreView):
    model = Work
    plugin_model = WorkAppContentPlugin


class WorkDetail(AllinkBaseDetailView):
    model = Work


def export_pdf(request, id):
    date = (datetime.date.today().strftime('%d_%m_%Y'))

    item = Work.objects.get(id=id)

    pdf = PdfWork(item, request)
    output = pdf.build()
    filename = '%s_%s.pdf' % (item.title.replace(' ', '_'), date)

    response = HttpResponse(output.getvalue(), content_type="application/pdf")
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
