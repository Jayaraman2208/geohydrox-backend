from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """GeoHydroX custom user."""

    ROLE_CHOICES = [
        ("admin", "Administrator"),
        ("officer", "Field Officer"),
        ("analyst", "Analyst"),
        ("viewer", "Viewer"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="viewer")
    phone = models.CharField(max_length=20, blank=True)
    district = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username