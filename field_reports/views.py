from rest_framework import viewsets
from .models import FieldReport
from .serializers import 

class FieldReportViewSet(viewsets.ModelViewSet):
    queryset = FieldReport.objects.all()
    serializer_class = FieldReportSerializer

