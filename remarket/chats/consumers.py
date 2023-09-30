import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.db import transaction
from django.db.models import Q
from channels.db import database_sync_to_async
from chats.models import Chat, Message
from django.contrib.auth.models import User
from chats.serializers import MessageSerializer


class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        chat_pk = self.scope['url_route']['kwargs']['pk']
        self.group_name = f"chat_{chat_pk}"
        chat = await self.get_chat(chat_pk)

        if chat:
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive_json(self, content):
        chat_pk = self.scope['url_route']['kwargs']['pk']
        chat = await self.get_chat(chat_pk)

        if not chat:
            await self.close()
            return

        message_text = content.get('text')
        sender = content.get('sender')
        if not message_text:
            return

        message = await self.create_message(chat, message_text, sender)

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat.message',
                'message': message,
            }
        )

    async def chat_message(self, event):
        await self.send_json(content=event['message'])

    @database_sync_to_async
    def get_chat(self, chat_pk):
        try:
            return Chat.objects.get(pk=chat_pk)
        except Chat.DoesNotExist:
            return None

    @database_sync_to_async
    def create_message(self, chat, message_text, sender):
        sender = User.objects.get(pk=sender)
        message = Message.objects.create(
            chat=chat, sender=sender, text=message_text)
        serializer = MessageSerializer(message)
        return serializer.data
