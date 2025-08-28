from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    HospitalRegisterView,
    ResourceStatusUpdateView,
    EmergencyRequestCreateView,
    hospital_finder,
)

urlpatterns = [
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/hospital/", HospitalRegisterView.as_view(), name="hospital_register"),
    path("resources/update/", ResourceStatusUpdateView.as_view(), name="resource_update"),
    path("emergency/request/", EmergencyRequestCreateView.as_view(), name="emergency_request"),
    path("hospital/finder/", hospital_finder, name="hospital_finder"),
]
