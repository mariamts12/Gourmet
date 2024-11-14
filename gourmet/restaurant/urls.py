from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (MainCategoryViewSet, MealViewSet, RestaurantsViewSet,
                    SubcategoryViewSet)

app_name = "restaurant"
router = DefaultRouter()
router.register(r"meals", MealViewSet, basename="meals")
router.register(r"categories", MainCategoryViewSet, basename="categories")
router.register(r"subcategories", SubcategoryViewSet, basename="subcategories")
router.register(r"restaurants", RestaurantsViewSet, basename="restaurants")

urlpatterns = [
    # path("restaurants/", RestaurantsView.as_view(), name="restaurants"),
    path("", include(router.urls), name="router"),
    # path("category/<slug:slug>", CategoryView.as_view(), name="subcategory_listing"),
    # path("category/", CategoryView.as_view(), name="subcategory_detail"),
]
