from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django_tables2 import SingleTableMixin, SingleTableView, MultiTableMixin
from django_tables2.export.views import ExportMixin, TableExport

from api.models import User, Camper, Transaction
from .tables import CamperTable

# Create your views here.
class TemplateView(TemplateView):
    template_name = 'portal/index.html'

    def renderTables(self):
        context = super()

#ministries
#camp
class CampView(MultiTableMixin, TemplateView):
    template_name = 'portal/camp.html'

    model = Camper
    tables = [
        CamperTable(Camper.objects.all().filter(level='0')),
        CamperTable(Camper.objects.all().filter(level='1')),
        CamperTable(Camper.objects.all()),
    ]

class CamperDetail(DetailView):
    model = Camper

class CamperExport(ExportMixin, SingleTableView):
    model = Camper
    table_class = CamperTable
    table_data = model.objects.all()
    export_name = 'campers'
    export_trigger_param = 'csv'
    template_name = 'django_tables2/bootstrap.html'

#cash
