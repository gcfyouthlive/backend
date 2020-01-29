from django.urls import include, path
from . import views


urlpatterns = [
    path(r'', views.index, name='camp2020_index'),
]