from django.urls import path
from products.views import ProductListView, ProductRetrieveView

urlpatterns = [
    path('', ProductListView.as_view(), name='listing-list'),
    path('<slug:slug>/', ProductRetrieveView.as_view(),
         name='listing-retrieve'),
]
