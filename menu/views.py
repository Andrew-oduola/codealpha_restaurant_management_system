from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import MenuItemSerializer
from .models import MenuItem


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
