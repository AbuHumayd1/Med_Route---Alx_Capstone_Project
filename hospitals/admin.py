from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ResourceStatus

@admin.register(ResourceStatus)
class ResourceStatusAdmin(admin.ModelAdmin):
    list_display = ("hospital", "beds", "icu_beds", "oxygen_cylinders", "available_doctors")
