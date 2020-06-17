import django_filters
from .models import *
from django_filters import DateFilter, CharFilter
class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = 'date', lookup_expr = 'gte')
    end_date = DateFilter(field_name = 'date', lookup_expr = 'lte')
    description = CharFilter(field_name = 'description', lookup_expr = 'icontains')
    class Meta:
        model = Order
        fields = '__all__'#all like the model form
        exclude = ['customer', 'date']

