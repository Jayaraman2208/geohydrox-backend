from django.db import models
from django.contrib.auth import get_user_model
from assets.models import Asset
User = get_user_model()

class FieldReport(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name="field_reports")
    submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to="field_reports/%Y/%m/")
    latitude = models.FloatField()
    longitude = models.FloatField()
    captured_at = models.DateTimeField()
    water_level = models.CharField(max_length=50, blank=True)
    ai_classification = models.CharField(max_length=100, blank=True)
    ai_confidence = models.FloatField(null=True, blank=True)
    def __str__(self): return f"Report on {self.asset.name}"