from rest_framework import viewsets
from .models import SatelliteScene
from .serializers import 

class SatelliteSceneViewSet(viewsets.ModelViewSet):
    queryset = SatelliteScene.objects.all()
    serializer_class = SatelliteSceneSerializer

