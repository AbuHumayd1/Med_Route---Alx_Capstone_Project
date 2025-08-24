from django.urls import path
from .views import EmergencyRequestCreateView, EmergencyRequestListView

urlpatterns = [
    path('requests/', EmergencyRequestCreateView.as_view(), name='create_request'),
    path('requests/all/', EmergencyRequestListView.as_view(), name='list_requests'),
]
