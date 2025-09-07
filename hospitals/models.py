from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from accounts.models import CustomUser


from django.db import models

class Hospital(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='hospital_profile',
        limit_choices_to={'role': 'hospital_admin'},
        null=True, blank=True
    )
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    capacity = models.PositiveIntegerField(default=0)  # total bed capacity
    available_beds = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class ResourceStatus(models.Model):
    hospital = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'hospital_admin'},
        related_name="resource_status"
    )
    beds = models.IntegerField(default=0)
    icu_beds = models.IntegerField(default=0)
    oxygen_cylinders = models.IntegerField(default=0)
    available_doctors = models.IntegerField(default=0)  # match serializer

    def __str__(self):
        return f"Resources for {self.hospital.username}"



# Emergency Requests
class EmergencyRequest(models.Model):
    patient_name = models.CharField(max_length=255)
    patient_condition = models.TextField()
    location_lat = models.FloatField()  
    location_long = models.FloatField() 
    required_specialists = models.PositiveIntegerField(default=0)
    required_icu = models.BooleanField(default=False)
    required_oxygen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.patient} → {self.hospital} ({self.status})"

    def __str__(self):
        return f"Emergency: {self.patient_name}"



class TransferLog(models.Model):
    patient_name = models.CharField(max_length=255)  # store name if no Patient model yet
    from_hospital = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="transfers_from"
    )
    to_hospital = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="transfers_to"
    )
    transferred_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transferred_by_user"
    )

    reason = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.patient_name} → {self.to_hospital} ({self.timestamp:%Y-%m-%d %H:%M})"
