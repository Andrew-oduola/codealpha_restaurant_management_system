from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import TableSerializer
from .models import Table

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


