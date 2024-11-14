import django_filters

from .models import Meal, Subcategory


class MealFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    category_name = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Meal
        fields = ['name', 'category_name']


class SubcategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    parent_name = django_filters.CharFilter(field_name='parent__name', lookup_expr='icontains')

    class Meta:
        model = Subcategory
        fields = ['name', 'parent_name']
