from rest_framework import serializers

from .models import Ingredient, MainCategory, Meal, Restaurant, Subcategory


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name"]

    def create(self, validated_data):
        restaurant = Restaurant(
            name=validated_data["name"],
            address=validated_data["address"],
            phone_number=validated_data["phone_number"],
            cover_photo=validated_data["cover_photo"],
        )
        restaurant.save()
        return restaurant


class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        action = self.context.get("view").action

        if action not in ["create", "update"]:
            # Keep only 'id' and 'name' for non-create/update actions
            fields_to_keep = ["id", "name"]
            fields = {key: fields[key] for key in fields_to_keep}

        return fields

    def create(self, validated_data):
        category = MainCategory(
            name=validated_data["name"], restaurant=validated_data["restaurant"]
        )
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.restaurant = validated_data.get("restaurant", instance.photo)
        instance.save()

        return instance


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        action = self.context.get("view").action

        if action not in ["create", "update"]:
            # Keep only 'id' and 'name' for non-create/update actions
            fields_to_keep = ["name", "cover_photo"]
            fields = {key: fields[key] for key in fields_to_keep}

        return fields

    def create(self, validated_data):
        sub = Subcategory(
            name=validated_data["name"],
            cover_photo=validated_data["cover_photo"],
            parent=validated_data["parent"],
        )
        sub.save()
        return sub

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.cover_photo = validated_data.get("cover_photo", instance.cover_photo)
        instance.parent = validated_data.get("parent", instance.parent)
        instance.save()

        return instance


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

    def create(self, validated_data):
        ingredient = Ingredient(name=validated_data["name"])
        ingredient.save()
        return ingredient


class MealSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True, read_only=True)

    class Meta:
        model = Meal
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        action = self.context.get("view").action

        if action not in ["create", "update"]:
            # Keep only 'id' and 'name' for non-create/update actions
            fields_to_keep = ["name", "photo", "ingredients"]
            fields = {key: fields[key] for key in fields_to_keep}

        return fields

    def create(self, validated_data):
        meal = Meal(
            name=validated_data["name"],
            price=validated_data["price"],
            photo=validated_data["photo"],
            category=validated_data["category"],
        )
        meal.save()
        return meal

    def update(self, instance, validated_data):
        pass
