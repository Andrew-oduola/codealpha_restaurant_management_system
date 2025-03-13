from rest_framework import viewsets
from .serializers import InventoryReportSerializers, SalesReportSerializers
from .models import InventoryReport, SalesReport

# Create your views here.
class InventoryReportViewSet(viewsets.ModelViewSet):
    queryset = InventoryReport.objects.all()
    serializer_class = InventoryReportSerializers

class SalesReportViewSet(viewsets.ModelViewSet):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializers

