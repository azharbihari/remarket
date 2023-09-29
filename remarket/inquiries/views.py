from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from interests.models import Interest
from inquiries.serializers import InquirySerializer
from products.models import Product
from django.shortcuts import get_object_or_404


class InquiryListView(generics.ListAPIView):
    queryset = Interest.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Interest.objects.filter(product__seller=self.request.user)


# class InterestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = InterestSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Interest.objects.filter(user=self.request.user)
