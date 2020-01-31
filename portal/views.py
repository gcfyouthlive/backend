from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django_tables2 import SingleTableView, SingleTableMixin

from api.models import Camper
from .tables import CamperTable

# Create your views here.
def index(TemplateView):
    return render(request, 'portal/index.html')

#ministries
def camp(request):
    query_hs = Camper.objects.all().filter(level='0')
    query_col = Camper.objects.all().filter(level='1')
    return render(request, 'portal/camp.html', locals())

class camper(TemplateView):
    template_name = 'portal/camp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query_hs'] = Camper.objects.all().filter(level='0')
        context['query_col'] = Camper.objects.all().filter(level='1')
        context['query_all'] = Camper.objects.all()
        return context

class camperDetail(DetailView):
    model = Camper
