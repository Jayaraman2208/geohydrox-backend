from django.db import models
from watersheds.models import Watershed


class Asset(models.Model):
    ASSET_TYPES = [
        ("check_dam", "Check Dam"),
        ("pond", "Farm Pond"),
        ("bund", "Water Bund"),
        ("trench", "Contour Trench"),
        ("tank", "Percolation Tank"),
        ("other", "Other"),
    ]
    STATUS = [
        ("planned", "Planned"),
        ("constructed", "Constructed"),
        ("functional", "Functional"),
        ("damaged", "Damaged"),
    ]
    watershed = models.ForeignKey(Watershed, on_delete=models.CASCADE, related_name="assets")
    name = models.CharField(max_length=200)
    asset_type = models.CharField(max_length=30, choices=ASSET_TYPES, default="other")
    status = models.CharField(max_length=20, choices=STATUS, default="planned")
    latitude = models.FloatField()
    longitude = models.FloatField()
    capacity_cubic_m = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_asset_type_display()} - {self.name}"