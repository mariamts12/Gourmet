from django.core.validators import MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=True)
    cover_photo = VersatileImageField(upload_to="restaurants/", null=True, blank=True)


class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    cover_photo = VersatileImageField(upload_to="categories/", null=True, blank=True)
    parent = models.ForeignKey(MainCategory, on_delete=models.CASCADE)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)


class Meal(models.Model):
    name = models.CharField(max_length=100)
    photo = VersatileImageField(upload_to="meals/", null=True, blank=True)
    price = models.DecimalField(
        validators=[MinValueValidator(0)], decimal_places=2, max_digits=5
    )
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
