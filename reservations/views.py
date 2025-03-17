from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.utils.dateparse import parse_datetime
from .serializers import ReservationSerializer
from .models import Reservation
from tables.models import Table
from tables.serializers import TableSerializer
from .permissions import IsAdminOrReadOnly



class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='available-tables', url_name='available-tables')
    def get_available_tables(self, request):
        reservation_time = request.query_params.get('reservation_time')
        party_size = request.query_params.get('party_size')
        if not reservation_time or not party_size:
            return Response({'error': 'Please provide reservation_time and party_size'}, status=status.HTTP_400_BAD_REQUEST)
        
        reservation_time = parse_datetime(reservation_time)
        if not reservation_time:
            return Response({'error': 'Invalid reservation_time format'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            party_size = int(party_size)
        except ValueError:
            return Response({'error': 'party_size must be an integer'}, status=status.HTTP_400_BAD_REQUEST)
        
        available_tables = Reservation.get_available_tables(reservation_time, party_size)
        serializer = TableSerializer(available_tables, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


