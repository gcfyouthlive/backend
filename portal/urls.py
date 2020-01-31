from django.urls import include, path
from . import views



urlpatterns = [
    path(r'', views.index, name='portal_index'),
    path(r'camp/', views.camper.as_view(), name='portal_camp'),
]