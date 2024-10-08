from .models import Dish,Restaurant,Proteine,Fruit

from .serializer import DishSerializer ,RestaurantSerailizer,ProteineSerializer,FruitSerializer

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class RestarantView(viewsets.ModelViewSet):
    permission_classes =[AllowAny]
    serializer_class = RestaurantSerailizer
    queryset = Restaurant.objects.all()


class DishView(viewsets.ModelViewSet):
    permission_classes =[AllowAny]
    serializer_class = DishSerializer
    queryset = Dish.objects.all()

    @action(detail=True, methods=['post'], url_path='valid')
    def dish_choise(self,request,pk =None):

        try:
            instance = self.get_object()
            instance.is_choise = True
            instance.save()

            serializer = self.get_serializer(instance)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Dish.DoesNotExist:  
            return Response({"detail": "Dish not found"}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=True, methods=['post'], url_path='disable')
    def desabled_choise(self,request,pk=None):

        try:
            instance = self.get_object()
            instance.is_choise = False
            instance.save()

            serializer = self.get_serializer(instance)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Dish.DoesNotExist:  
            return Response({"detail": "Dish not found"}, status=status.HTTP_404_NOT_FOUND)



class ProteineView(viewsets.ModelViewSet):
    permission_classes =[AllowAny]
    serializer_class = ProteineSerializer
    queryset = Proteine.objects.all()

class FruitView(viewsets.ModelViewSet):
    permission_classes =[AllowAny]
    serializer_class = FruitSerializer
    queryset = Fruit.objects.all()