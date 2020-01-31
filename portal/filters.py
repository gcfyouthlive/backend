import django_filters
from api.models import Camper

class CamperFilter(django_filters.FilterSet):
    level = django_filters.NumberFilter(field_name='level')

    class Meta:
        model = Camper
        fields = ['level', 'year','paid','waiver']