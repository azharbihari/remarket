from rest_framework import serializers
from products.models import Category, Product
from authentications.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    condition = serializers.CharField(
        source='get_condition_display', read_only=True)

    availability = serializers.CharField(
        source='get_availability_display', read_only=True)
    delivery_option = serializers.CharField(
        source='get_delivery_option_display', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
