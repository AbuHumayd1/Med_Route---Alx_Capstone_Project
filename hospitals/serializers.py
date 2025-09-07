from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser, ResourceStatus, EmergencyRequest, TransferLog, Hospital


class HospitalUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'name', 'address', 'latitude', 'longitude']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class ResourceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceStatus
        fields = ['id', 'hospital', 'beds', 'icu_beds', 'oxygen_cylinders', 'available_doctors']
        read_only_fields = ['hospital']


class EmergencyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyRequest
        fields = ['id', 'patient_name', 'patient_condition', 'location_lat', 'location_long', 'status', 'assigned_hospital']


class TransferLogSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source="patient.full_name", read_only=True)
    from_hospital_name = serializers.CharField(source="from_hospital.name", read_only=True)
    to_hospital_name = serializers.CharField(source="to_hospital.name", read_only=True)

    class Meta:
        model = TransferLog
        fields = [
            "id",
            "patient", "patient_name",
            "from_hospital", "from_hospital_name",
            "to_hospital", "to_hospital_name",
            "transferred_by",
            "reason",
            "timestamp",
        ]
        read_only_fields = ["timestamp", "transferred_by"]


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"
