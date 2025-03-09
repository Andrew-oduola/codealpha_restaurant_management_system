from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F
from .serializers import InventorySerializer
from .models import Inventory

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    @action(detail=False, methods=['get'], url_path='low-stock', url_name='low_stock')
    def low_stock(self, request):
        low_stock_items = Inventory.objects.filter(quantity__lt=F('reorder_level'))
        serializer = self.get_serializer(low_stock_items, many=True)
        return Response(serializer.data)

