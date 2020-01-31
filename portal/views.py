from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django_tables2 import SingleTableMixin, MultiTableMixin

from api.models import Camper, User
from .tables import CamperTable

# Create your views here.
def index(TemplateView):
    return render(request, 'portal/index.html')

#ministries
def camp(request):
    query_hs = Camper.objects.all().filter(level='0')
    query_col = Camper.objects.all().filter(level='1')
    return render(request, 'portal/camp.html', locals())

class camper(MultiTableMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query_hs'] = Camper.objects.all().filter(level='0')
        context['query_col'] = Camper.objects.all().filter(level='1')
        context['query_all'] = Camper.objects.all()
        return context

    template_name = 'portal/camp.html'
    model = Camper
    tables = [
        CamperTable(Camper.objects.all()),
        CamperTable(Camper.objects.all().filter(level='0')),
        CamperTable(Camper.objects.all().filter(level='1')),
    ]

class camperDetail(DetailView):
    model = Camper
