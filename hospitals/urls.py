from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import (
    HospitalRegisterView,
    ResourceStatusUpdateView,
    EmergencyRequestCreateView,
    hospital_finder,
    ResourceStatusViewSet,
    TransferLogViewSet,
    HospitalViewSet,
)

router = DefaultRouter()
router.register(r'hospitals', HospitalViewSet, basename='hospital')
router.register(r'resource-status', ResourceStatusViewSet, basename='resource-status')
router.register(r'transfer-logs', TransferLogViewSet, basename='transfer-log')

urlpatterns = [
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/hospital/", HospitalRegisterView.as_view(), name="hospital_register"),
    path("resources/update/", ResourceStatusUpdateView.as_view(), name="resource_update"),
    path("emergency/request/", EmergencyRequestCreateView.as_view(), name="emergency_request"),
    path("hospital/finder/", hospital_finder, name="hospital_finder"),
    path('', include(router.urls)),
]
