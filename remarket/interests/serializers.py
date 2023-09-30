from rest_framework import serializers
from interests.models import Interest
from rest_framework.fields import CurrentUserDefault
from products.serializers import ProductSerializer
from chats.serializers import ChatSerializer
from authentications.serializers import UserSerializer


class InterestSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    chat = ChatSerializer()

    class Meta:
        model = Interest
        fields = '__all__'


class InterestCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Interest
        fields = '__all__'
