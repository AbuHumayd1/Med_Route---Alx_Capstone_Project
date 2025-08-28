from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from math import radians, sin, cos, sqrt, atan2
from .models import ResourceStatus, EmergencyRequest
from django.http import JsonResponse
from .serializers import (
    HospitalUserSerializer,   # instead of HospitalRegisterSerializer
    ResourceStatusSerializer,
    EmergencyRequestSerializer,
)

def health(request):
    return JsonResponse({"status": "ok"})

HospitalUser = get_user_model()

# Hospital Registration
class HospitalRegisterView(generics.CreateAPIView):
    queryset = HospitalUser.objects.all()
    serializer_class = HospitalUserSerializer   # change here too
    permission_classes = [permissions.AllowAny]


# Update Hospital Resources
class ResourceStatusUpdateView(generics.UpdateAPIView):
    serializer_class = ResourceStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        hospital = self.request.user
        resource, created = ResourceStatus.objects.get_or_create(hospital=hospital)
        return resource


# Emergency Request Creation
class EmergencyRequestCreateView(generics.CreateAPIView):
    queryset = EmergencyRequest.objects.all()
    serializer_class = EmergencyRequestSerializer
    permission_classes = [permissions.AllowAny]


# Utility function for distance calculation (Haversine)
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)
    a = sin(d_lat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


# Hospital Finder API (match nearest hospital with resources)
@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def hospital_finder(request):
    patient_lat = request.data.get("latitude")
    patient_lon = request.data.get("longitude")

    hospitals = HospitalUser.objects.filter(is_hospital=True)
    nearest_hospital = None
    min_distance = float("inf")

    for hospital in hospitals:
        if hospital.latitude and hospital.longitude:
            distance = calculate_distance(patient_lat, patient_lon, hospital.latitude, hospital.longitude)
            if distance < min_distance:
                min_distance = distance
                nearest_hospital = hospital

    if nearest_hospital:
        resource = getattr(nearest_hospital, "resources", None)
        return Response({
            "hospital": nearest_hospital.name,
            "address": nearest_hospital.address,
            "distance_km": round(min_distance, 2),
            "resources": ResourceStatusSerializer(resource).data if resource else {}
        })
    return Response({"error": "No hospital found"}, status=404)

