import django_tables2 as tables
from api.models import Camper

class CamperTable(tables.Table):
    class Meta:
        model = Camper
        #fields = ['']