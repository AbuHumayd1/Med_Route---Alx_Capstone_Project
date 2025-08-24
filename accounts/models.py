from django.contrib.auth.models import AbstractUser
from django.db import models

class HospitalUser(AbstractUser):
    hospital_name = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.hospital_name or self.username
