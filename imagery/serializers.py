from rest_framework import serializers
from .models import SatelliteScene

class SatelliteSceneSerializer(serializers.ModelSerializer):
    class Meta:
        model = SatelliteScene
        fields = '__all__'

