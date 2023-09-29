from rest_framework import serializers
from products.models import Category, Product
from authentications.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    featured_image = serializers.ImageField(required=False)
    seller = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), write_only=True
    )

    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than zero")
        return value
