from django.urls import path
from interests.views import InterestCreateView, InterestRetrieveUpdateDestroyAPIView, InterestListView

urlpatterns = [
    path('', InterestListView.as_view(), name='interest-list-'),
    path('create/', InterestCreateView.as_view(), name='interest-create'),
    path('<int:pk>/', InterestRetrieveUpdateDestroyAPIView.as_view(),
         name='interest-retrieve-update-destroy'),

]
