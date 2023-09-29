from django.urls import path
from inquiries.views import InquiryListView

urlpatterns = [
    path('', InquiryListView.as_view(), name='inquiry-list'),
    # path('<int:pk>/', InterestRetrieveUpdateDestroyAPIView.as_view(),
    #      name='interest-retrieve-update-destroy'),
]
