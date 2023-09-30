from django.db import models
from django.contrib.auth.models import User
from interests.models import Interest


class Chat(models.Model):
    interest = models.OneToOneField(Interest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('buyer', 'Buyer'),
                                                    ('seller', 'Seller')])
    status = models.CharField(max_length=10, choices=[(
        'active', 'Active'), ('archived', 'Archived'), ('closed', 'Closed')], default='active')
    unread_messages_count = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
