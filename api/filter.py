from django_filters import rest_framework as filter
from .models import Student


class FilterStudent(filter.FilterSet):
    university_id = filter.CharFilter(field_name='university_id', lookup_expr='in')

    class Meta:
        model = Student
        fields = ("university_id", )