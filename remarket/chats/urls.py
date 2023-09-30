from django.urls import path
from chats.views import ChatCreateView, ChatRetrieveView

urlpatterns = [
    path('', ChatCreateView.as_view(), name='chat-create'),
    path('<int:pk>/', ChatRetrieveView.as_view(), name='chat-retrieve'),
]
