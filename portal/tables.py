import django_tables2 as tables
from api.models import Camper, User

class CamperTable(tables.Table):
    class Meta:
        model = Camper
        exclude = ('id',)
        #fields = ['firstname','lastname']