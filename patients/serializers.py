from rest_framework import serializers
from .models import EmergencyRequest

class EmergencyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyRequest
        fields = '__all__'
        read_only_fields = ['id', 'request_time', 'status']
