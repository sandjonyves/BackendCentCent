
import django.dispatch
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print('Connexion WebSocket établie')
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': 'Bienvenue dans le chat! dsdds'
        }))

    async def disconnect(self, close_code):
        print('Client déconnecté', close_code)

    async def receive(self, text_data):
        print('Message reçu:', text_data)
        try:
            data = json.loads(text_data)  
            message = data.get('message', '')  

            response_message = f"Vous avez dit : {message}"
            print(response_message)

            await self.send(text_data=json.dumps({
                'message': response_message
            }))
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'error': 'Erreur de format de données.'
            }))


class NotificationStudentConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.student_id = self.scope['url_route']['kwargs']['student_id']
        self.group_name = f"student_{self.student_id}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
                f'student_{self.student_id}', 
            {"type":'order_validated',
            'message':'hsghdghsghdghhsgdhsghgdhsdsddddddddddddddddddd'
        })
        await self.send(text_data=json.dumps({
            'message': 'Bienvenue dans le chat de groupe!'
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        print('Client déconnecté', close_code)

    async def order_validated(self, event):
        message = event['message']
        print('Message reçu pour validation de commande:', message)

        await self.send(text_data=json.dumps({
            'message': message
        }))



class AdminConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        from store.models import Dish

        await self.channel_layer.group_add('notifications', self.channel_name)

        choise_dishes =await Dish.get_choise()
        if choise_dishes:  #
            await self.channel_layer.group_send(
                "notifications",
                {
                    'type': 'dish_choice',
                    'message':choise_dishes
                }
            )
        else:
            print("Aucun plat choisi disponible.")

        await self.accept()


        # async def receive(self, text_data):
        # # Appeler directement la méthode asynchrone avec await
        # choise_dishes = await Dish.get_choise()
        
        # # Envoyer les plats au client WebSocket
        # await self.send(text_data=json.dumps({
        #     'choise_dishes': choise_dishes
        # }))
       

    async def disconnect(self, code):
        print('Admin déconnecté', code)
        await self.channel_layer.group_discard('notifications', self.channel_name)

    async def dish_choice(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))