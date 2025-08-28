from django.db import models
from django.contrib.auth.models import AbstractUser



# One-to-One with Hospital
from django.db import models
from accounts.models import HospitalUser   # <-- ADD THIS IMPORT


class ResourceStatus(models.Model):
    hospital = models.OneToOneField(
        HospitalUser,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'hospital_admin'},  # ensures only hospital admins can have resources
        related_name="resource_status"
    )
    beds = models.IntegerField(default=0)
    icu_beds = models.IntegerField(default=0)
    oxygen_cylinders = models.IntegerField(default=0)
    available_doctors = models.IntegerField(default=0)

    def __str__(self):
        return f"Resources for {self.hospital.username}"



# Emergency Requests
class EmergencyRequest(models.Model):
    patient_name = models.CharField(max_length=255)
    patient_condition = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    required_specialists = models.PositiveIntegerField(default=0)
    required_icu = models.BooleanField(default=False)
    required_oxygen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Emergency: {self.patient_name}"
