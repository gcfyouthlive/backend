from django.urls import include, path
from rest_framework import routers
from . import views

# Routers
router = routers.DefaultRouter()

# Users
router.register(r'users', views.UserViewSet)
# Campers
router.register(r'campers', views.CamperViewSet)
# Ask.YouthLIVE
router.register(r'ask', views.AyliveViewSet)
# Events
router.register(r'events',views.EventsViewSet)
# Transaction
router.register(r'transaction', views.TransactionViewSet)
#Reciept
router.register(r'reciept', views.RecieptViewSet)

# Browsable API
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
