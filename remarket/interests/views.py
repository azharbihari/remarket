from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from interests.models import Interest
from interests.serializers import InterestSerializer, InterestCreateSerializer
from products.models import Product
from django.shortcuts import get_object_or_404


class InterestListView(generics.ListAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Interest.objects.filter(user=self.request.user)


class InterestCreateView(generics.CreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestCreateSerializer
    permission_classes = [IsAuthenticated]


class InterestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Interest.objects.filter(user=self.request.user)
