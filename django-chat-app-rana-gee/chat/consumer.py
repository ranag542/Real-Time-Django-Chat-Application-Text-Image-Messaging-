import json
import base64
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.core.files.base import ContentFile
from .models import Message, Room, Registratoin

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')
        user = text_data_json['user']
        image_data = text_data_json.get('image', None)

        if image_data:
            # Decode base64 image data
            image_data = image_data.split(';base64,')[-1]
            image_content = ContentFile(base64.b64decode(image_data), name="chat_image.png")
            
            # Save the message with the image
            saved_message = await self.save_message(user, self.room_name, message, image=image_content)
            image_url = saved_message.image.url if saved_message.image else None
        else:
            # Save the message without an image
            saved_message = await self.save_message(user, self.room_name, message)
            image_url = None

        # Send the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user,
                'image_url': image_url,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        image_url = event.get('image_url', None)

        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'image_url': image_url,
        }))

    @sync_to_async
    def save_message(self, username, room_name, message, image=None):
        user = Registratoin.objects.get(user_name=username)
        room, _ = Room.objects.get_or_create(name=room_name)

        return Message.objects.create(user=user, room=room, content=message, image=image)
