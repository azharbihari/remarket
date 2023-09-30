from django.urls import path

from chats.consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<int:pk>/', ChatConsumer.as_asgi()),
]
