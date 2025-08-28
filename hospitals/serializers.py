from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import HospitalUser, ResourceStatus, EmergencyRequest


class HospitalUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = HospitalUser
        fields = ['id', 'username', 'password', 'name', 'address', 'latitude', 'longitude']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class ResourceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceStatus
        fields = ['id', 'hospital', 'beds', 'icu_beds', 'oxygen_cylinders', 'specialists']
        read_only_fields = ['hospital']


class EmergencyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyRequest
        fields = ['id', 'patient_name', 'patient_condition', 'location_lat', 'location_long', 'status', 'assigned_hospital']

