from django.db import models
from django.conf import settings

class EmergencyRequest(models.Model):
    STATUS_CHOICES = [('P', 'Pending'), ('A', 'Assigned'), ('C', 'Completed')]
    CONDITION_CHOICES = [
        ('cardiac', 'Cardiac'),
        ('accident', 'Accident'),
        ('respiratory', 'Respiratory'),
        ('diabetic', 'Diabetic'),
        ('birth', 'Birth'),
        ('stroke', 'Stroke'),
        ('other', 'Other'),
    ]

    request_time = models.DateTimeField(auto_now_add=True)
    reported_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='reports'
    )
    condition_type = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return f"{self.condition_type} @ ({self.latitude},{self.longitude}) [{self.get_status_display()}]"
