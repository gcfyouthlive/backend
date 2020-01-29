from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer,CamperSerializer,AyliveSerializer, EventsSerializer, TransactionSerializer, RecieptSerializer
from .models import User,Camper,Aylive,Events,Transaction,Reciept

# API
# Users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('lastname')
    serializer_class = UserSerializer

# Campers
class CamperViewSet(viewsets.ModelViewSet):
    queryset = Camper.objects.all().order_by('lastname')
    serializer_class = CamperSerializer

# Ask.YouthLIVE
class AyliveViewSet(viewsets.ModelViewSet):
    queryset = Aylive.objects.all().order_by('timestamp')
    serializer_class = AyliveSerializer

# Events
class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('datetime')
    serializer_class = EventsSerializer

# Transaction
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('trans_date')
    serializer_class = TransactionSerializer

#RReciepts
class RecieptViewSet(viewsets.ModelViewSet):
    queryset = Reciept.objects.all().order_by('reci_date')
    serializer_class = RecieptSerializer

