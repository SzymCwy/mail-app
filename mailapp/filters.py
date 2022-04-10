from django_filters import rest_framework as filters
from django import forms
from .models import Email


class EmailFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name='date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}))
    date_till = filters.DateFilter(field_name='date', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}))
    sent = filters.BooleanFilter(field_name='sent_date', lookup_expr='isnull')

    class Meta:
        model = Email
        fields = ['sent']
