from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import EmergencyRequest
from .serializers import EmergencyRequestSerializer

class EmergencyRequestCreateView(generics.CreateAPIView):
    queryset = EmergencyRequest.objects.all()
    serializer_class = EmergencyRequestSerializer
    permission_classes = [permissions.AllowAny]  # Later: tighten if needed

class EmergencyRequestListView(generics.ListAPIView):
    queryset = EmergencyRequest.objects.all().order_by('-request_time')
    serializer_class = EmergencyRequestSerializer
    permission_classes = [permissions.IsAdminUser]
