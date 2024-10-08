from django.urls import path,include
from .views import *
from rest_framework import routers


route = routers.SimpleRouter()


route.register('restaurant',RestarantView,basename='restaurant')
route.register('dish',DishView,basename='dish')
route.register('proteine',ProteineView,basename='proteine')
route.register('fruit',FruitView,basename='fruit')


urlpatterns = [
      path('',include(route.urls)),

]