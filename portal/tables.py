import django_tables2 as tables
from api.models import Camper, Transaction

class CamperTable(tables.Table):
    class Meta:
        model = Camper
        exclude = ('id',)
        #fields = ['firstname','lastname']

class TransactionTable(tables.Table):
    class Meta:
        model = Transaction
        exclude = ('id',)
        # fields = ['firstname','lastname']