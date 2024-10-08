from .views import orderView

from django.urls import path,include

from rest_framework import routers


route =routers.SimpleRouter()

route.register('order',orderView)

urlpatterns =[
    path('',include(route.urls))
]