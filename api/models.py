from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import datetime, uuid

# Create your models here.

#Custom User
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=25, unique=True, blank=False)
    email = models.EmailField(_('email address'),unique=True, blank=False)
    firstname = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100,blank=False)
    signup_date = models.DateField(auto_now_add=True,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','firstname','lastname',]

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='profile')
    cash_onhand = models.FloatField(blank=False, default=0)
    birthday = models.DateField(default=datetime.date.today)
    school = models.CharField(max_length=128)
    #0 hs, 1 col, 2 ya
    level = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)

# Ask.YouthLIVE
class Aylive(models.Model):
    question = models.TextField(max_length=255,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.questions

# Events System
class Events(models.Model):
    eventname = models.CharField(max_length=60, blank=False)
    datetime = models.DateTimeField()
    attendees = models.ManyToManyField('User',blank=True)

    def __str__(self):
        return self.eventname

# Reimbursment System
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,related_name='cash_user')

    trans_date = models.DateField(blank=False)
    purpose = models.CharField(max_length=254,blank=False)
    #yg, fl, fellowship
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True)


    def __str__(self):
        return self.purpose

class Reciept(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)

    acc_title = models.CharField(max_length=254, blank=False)
    # Hardcoded values
    reci_establishment = models.CharField(max_length=254, blank=False)
    reci_amt = models.FloatField(blank=False)
    reci_date = models.DateField(blank=False)
    reci_or = models.CharField(max_length=254)
    img = models.ImageField(blank=True)

# Camper
#class Campers(models.Model):