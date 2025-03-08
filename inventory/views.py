from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import InventorySerializer
from .models import Inventory

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

