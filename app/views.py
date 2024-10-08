import channels.generic.websocket
import json
from .models import Order
from .serializer import OrderSerialiser
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class orderView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = OrderSerialiser
    queryset = Order.objects.all()

    @action(detail=True, methods=['post'], url_path='valid')
    def order_valid(self, request, pk=None):
        try:
            instance = self.get_object()

            instance.status = True
            instance.save()


            # self.notify_student(instance.id, instance.student_id)

            serializer = self.get_serializer(instance)  
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Order.DoesNotExist:  
            return Response({"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

    def notify_student(self,order_id, student_id):
        channel_layer = get_channel_layer()
        print('ttttttttt',student_id.id)
        if channel_layer:
            async_to_sync(channel_layer.group_send)(
                f'student_{student_id.id}', 
            {
            "type":'order_validated',
            'message':'sssssssssssssssssssssssssssssssssssssssssssshsghdghsghdghhsgdhsghgdhsdsddddddddddddddddddd'
        })
        else:
            print("Erreur : Layer de canaux non disponible.")


    