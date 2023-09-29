from rest_framework import serializers
from interests.models import Interest
from rest_framework.fields import CurrentUserDefault


class InterestSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Interest
        fields = '__all__'
