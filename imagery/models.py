from django.db import models
from watersheds.models import Watershed

class SatelliteScene(models.Model):
    SOURCES = [("sentinel2","Sentinel-2"),("landsat8","Landsat-8"),("srishti","SRISHTI-DRISHTI")]
    watershed = models.ForeignKey(Watershed, on_delete=models.CASCADE, related_name="scenes")
    source = models.CharField(max_length=20, choices=SOURCES, default="sentinel2")
    acquired_at = models.DateField()
    cloud_cover = models.FloatField(default=0)
    tile_url = models.URLField(blank=True)
    ndvi_mean = models.FloatField(null=True, blank=True)
    def __str__(self): return f"{self.get_source_display()} - {self.watershed.code}"