from django.shortcuts import render
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Restaurant, Meal, MainCategory, Subcategory
from .serializers import RestaurantSerializer, MealSerializer, MainCategorySerializer, SubcategorySerializer


class RestaurantsView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    authentication_classes = [SessionAuthentication]


class MealViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Meal.objects.prefetch_related("ingredients")
    serializer_class = MealSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action in ["create", "update"]:
            return [IsAuthenticated()]
        # Allow any user for listing and retrieving
        return [AllowAny()]

    def get_view_name(self):
        return "Menu"


class MainCategoryViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer
    authentication_classes = [SessionAuthentication]

    def get_permissions(self):
        if self.action in ["create", "update"]:
            return [IsAuthenticated()]
        # Allow any user for listing and retrieving
        return [AllowAny()]


class SubcategoryViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    authentication_classes = [SessionAuthentication]

    def get_permissions(self):
        if self.action in ["create", "update"]:
            return [IsAuthenticated()]
        # Allow any user for listing and retrieving
        return [AllowAny()]
