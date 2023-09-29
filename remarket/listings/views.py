from django.shortcuts import get_object_or_404
from rest_framework import generics
from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.parsers import MultiPartParser, FormParser


class IsSellerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.seller == request.user


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ListingListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated | IsSellerOrReadOnly]
    authentication_classes = [TokenAuthentication]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)


class ListingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated | IsSellerOrReadOnly]
    authentication_classes = [TokenAuthentication]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)
