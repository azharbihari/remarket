from django.shortcuts import get_object_or_404
from rest_framework import generics
from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer
from interests.models import Interest
from rest_framework import generics, status
from rest_framework.response import Response


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        user_has_interest = False
        if request.user.is_authenticated:
            user_has_interest = Interest.objects.filter(
                user=request.user, product=instance).exists()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['user_has_interest'] = user_has_interest

        return Response(data)
