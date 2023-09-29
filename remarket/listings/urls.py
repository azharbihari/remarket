from django.urls import path
from listings.views import ListingListCreateView, ListingRetrieveUpdateDestroyView

urlpatterns = [
    path('', ListingListCreateView.as_view(), name='listing-list-create'),
    path('<slug:slug>/', ListingRetrieveUpdateDestroyView.as_view(),
         name='listing-retrieve-update-destroy'),
]
