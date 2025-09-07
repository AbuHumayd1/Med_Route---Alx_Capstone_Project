from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from math import radians, sin, cos, sqrt, atan2
from django.http import JsonResponse
from .models import ResourceStatus, EmergencyRequest, TransferLog, Hospital
from .serializers import HospitalSerializer, ResourceStatusSerializer, TransferLogSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import (
    HospitalUserSerializer,
    ResourceStatusSerializer,
    EmergencyRequestSerializer,
    TransferLogSerializer,
)

def health(request):
    return JsonResponse({"status": "ok"})

HospitalUser = get_user_model()

class HospitalRegisterView(generics.CreateAPIView):
    queryset = HospitalUser.objects.all()
    serializer_class = HospitalUserSerializer
    permission_classes = [permissions.AllowAny]

class ResourceStatusUpdateView(generics.UpdateAPIView):
    serializer_class = ResourceStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        hospital = self.request.user
        resource, created = ResourceStatus.objects.get_or_create(hospital=hospital)
        return resource

class EmergencyRequestCreateView(generics.CreateAPIView):
    queryset = EmergencyRequest.objects.all()
    serializer_class = EmergencyRequestSerializer
    permission_classes = [permissions.AllowAny]

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)
    a = sin(d_lat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def hospital_finder(request):
    patient_lat = request.data.get("latitude")
    patient_lon = request.data.get("longitude")

    hospitals = HospitalUser.objects.filter(role="hospital_admin")
    nearest_hospital = None
    min_distance = float("inf")

    for hospital in hospitals:
        if hospital.latitude and hospital.longitude:
            distance = calculate_distance(patient_lat, patient_lon, hospital.latitude, hospital.longitude)
            if distance < min_distance:
                min_distance = distance
                nearest_hospital = hospital

    if nearest_hospital:
        resource = getattr(nearest_hospital, "resource_status", None)
        return Response({
            "hospital": nearest_hospital.name,
            "address": getattr(nearest_hospital, "address", ""),
            "distance_km": round(min_distance, 2),
            "resources": ResourceStatusSerializer(resource).data if resource else {}
        })
    return Response({"error": "No hospital found"}, status=404)

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ResourceStatusViewSet(viewsets.ModelViewSet):
    queryset = ResourceStatus.objects.all()
    serializer_class = ResourceStatusSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TransferLogViewSet(viewsets.ModelViewSet):
    queryset = TransferLog.objects.all()
    serializer_class = TransferLogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

from django.shortcuts import render

def home(request):
    return render(request, "home.html") 
