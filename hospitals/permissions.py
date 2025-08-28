from rest_framework.permissions import BasePermission

class IsHospital(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "hospital"

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
