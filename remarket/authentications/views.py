from datetime import date
from interests.models import Interest
from chats.models import Chat, Message
from products.models import Product, Category
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from authentications.serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class RegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Incorrect username or password. Please try again.'}, status=status.HTTP_401_UNAUTHORIZED)


class UserDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InsightAPIView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        total_products_listed = Product.objects.filter(
            seller=self.request.user).count()
        inquiry_count = Interest.objects.filter(
            product__seller=self.request.user).count()

        inquries_today = Interest.objects.filter(
            product__seller=self.request.user, created_at__date=date.today()
        ).count()

        products_with_no_inquiries = Product.objects.filter(
            interests__isnull=True, seller=self.request.user).count()
        insights = {
            'total_products_listed': total_products_listed,
            'inquiry_count': inquiry_count,
            'inquries_today': inquries_today,
            'products_with_no_inquiries': products_with_no_inquiries
        }

        return Response(insights)
