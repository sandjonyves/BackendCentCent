from . models import Dish, Restaurant , Proteine, Fruit
from rest_framework import serializers


class RestaurantSerailizer(serializers.ModelSerializer):

    class Meta:
        model  =  Restaurant
        fields = ('__all__')

class DishSerializer(serializers.ModelSerializer):

    restaurant = RestaurantSerailizer(read_only=True)
    class Meta:
        model = Dish
        fields = ('name','restaurant_id','restaurant','is_choise')

class ProteineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proteine
        fields = ('__all__')

class FruitSerializer(serializers.ModelSerializer):

    class Meta:
        model =Fruit
        fields = ('__all__')