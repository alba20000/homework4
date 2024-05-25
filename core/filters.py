import django_filters
from django.db.models import Q
from core import models


class Staff(django_filters.FilterSet):
    first_name = django_filters.CharFilter(label='Имя', lookup_expr='icontains')
    birthday_to = django_filters.DateFilter(field_name='date_of_birth', lookup_expr='lt')
    salary_from = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')
    fio = django_filters.CharFilter(method='fio_filter', label='ФИО')

    class Meta:
        model = models.Staff
        exclude = ('picture',)

    def fio_filter(self, queryset, value):
        return queryset.filter(Q(first_name__icontains=value) | Q(last_name__icontains=value) | Q(patronymic__icontains=value))
