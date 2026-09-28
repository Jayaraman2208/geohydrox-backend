from rest_framework import serializers
from .models import FieldReport

class FieldReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldReport
        fields = '__all__'

