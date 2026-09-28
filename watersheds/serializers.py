from rest_framework import serializers
from .models import Watershed, HealthScore

class WatershedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watershed
        fields = '__all__'

class HealthScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthScore
        fields = '__all__'

