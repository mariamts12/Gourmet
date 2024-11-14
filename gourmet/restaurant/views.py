from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .models import MainCategory, Meal, Restaurant, Subcategory
from .serializers import (MainCategorySerializer, MealSerializer,
                          RestaurantSerializer, SubcategorySerializer)


class RestaurantsView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    authentication_classes = [SessionAuthentication]


class MealViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Meal.objects.prefetch_related("ingredients")
    serializer_class = MealSerializer
    authentication_classes = [SessionAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "category__name"]

    def get_permissions(self):
        if self.action in ["create", "update"]:
            return [IsAuthenticated()]
        # Allow any user for listing and retrieving
        return [AllowAny()]

    def get_view_name(self):
        return "Menu"


class MainCategoryViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer
    authentication_classes = [SessionAuthentication]

    def get_permissions(self):
        if self.action in ["create", "update"]:
            return [IsAuthenticated()]
        # Allow any user for listing and retrieving
        return [AllowAny()]


class SubcategoryViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    authentication_classes = [SessionAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "parent__name"]

    def get_permissions(self):
        if self.action in ["create", "update"]:
            return [IsAuthenticated()]
        # Allow any user for listing and retrieving
        return [AllowAny()]
