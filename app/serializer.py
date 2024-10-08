from .models import Order

from account.serializers import EtudiantSerializer

from rest_framework import serializers


class OrderSerialiser(serializers.ModelSerializer):

    etudiant=EtudiantSerializer(read_only=True)
    class Meta:
        model = Order
        fields =('id','order_date','status','operator','dish_number','etudiant_id','restaurant_id','etudiant')
    
 