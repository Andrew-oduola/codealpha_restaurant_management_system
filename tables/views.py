from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import TableSerializer
from .models import Table

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    @action(detail=False, methods=['get'], url_path='available', url_name='available')
    def available_table(self, request):
        available_tables = Table.objects.filter(is_occupied=False)
        serializer = self.get_serializer(available_tables, many=True)
        return Response(serializer.data)
