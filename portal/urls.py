from django.urls import include, path
from . import views


urlpatterns = [
    path(r'index/', views.index, name='portal_index'),
]