from django.urls import include, path
from . import views



urlpatterns = [
    path(r'', views.TemplateView.as_view(template_name='portal/index.html'), name='portal_index'),

    #cash
    path(r'cash/', views.TemplateView.as_view(template_name='portal/cash.html'), name='portal_cash'),

    #camp
    path(r'camp/', views.CampView.as_view(), name='portal_camp'),
    path(r'camp/?_export=csv&table=hs', views.CamperExport.as_view(table_data="Camper.objects.all().filter(level='0')")),
    path(r'camp/?_export=csv&table=col', views.CamperExport.as_view(table_data="Camper.objects.all().filter(level='1')")),
    path(r'camp/?_export=csv&table=all', views.CamperExport.as_view(table_data="Camper.objects.all()")),
]