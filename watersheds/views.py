from rest_framework import viewsets
from .models import Watershed, HealthScore
from .serializers import WatershedSerializer, HealthScoreSerializer

class WatershedViewSet(viewsets.ModelViewSet):
    queryset = Watershed.objects.all()
    serializer_class = WatershedSerializer

class HealthScoreViewSet(viewsets.ModelViewSet):
    queryset = HealthScore.objects.all()
    serializer_class = HealthScoreSerializer

