from django.urls import path
from interests.views import InterestListCreateView, InterestRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', InterestListCreateView.as_view(), name='interest-list-create'),
    path('<int:pk>/', InterestRetrieveUpdateDestroyAPIView.as_view(),
         name='interest-retrieve-update-destroy'),

]
