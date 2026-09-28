from django.db import models

class Watershed(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    area_hectares = models.FloatField(default=0)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.name} ({self.code})"

class HealthScore(models.Model):
    watershed = models.ForeignKey(Watershed, on_delete=models.CASCADE, related_name="health_scores")
    date = models.DateField()
    ndvi_score = models.FloatField(default=0)
    soil_moisture = models.FloatField(default=0)
    water_recharge = models.FloatField(default=0)
    composite_score = models.FloatField(default=0)
    def __str__(self): return f"{self.watershed.code} @ {self.date}"