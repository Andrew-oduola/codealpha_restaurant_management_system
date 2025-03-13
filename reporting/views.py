from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Sum
from orders.models import OrderItem
from reservations.models import Reservation     
from .serializers import InventoryReportSerializer, SalesReportSerializer
from .models import InventoryReport, SalesReport


# Create your views here.
class InventoryReportViewSet(viewsets.ModelViewSet):
    queryset = InventoryReport.objects.all()
    serializer_class = InventoryReportSerializer

    @action(detail=False, methods=['get'], url_path='popular-items', url_name='popular_items')
    def popular_items(self, request):
        popular_items = OrderItem.objects.values('menu_item').annotate(total_quantity=Count('quantity')).order_by('-total_quantity')[:10]
        return Response(popular_items)

    @action(detail=False, methods=['get'], url_path='reservation-trends', url_name='reservation_trends')
    def reservation_trends(self, request):
        reservation_trends = Reservation.objects.values('date').annotate(total_reservations=Count('id')).order_by('-total_reservations')[:10]
        return Response(reservation_trends)

    

class SalesReportViewSet(viewsets.ModelViewSet):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer

    @action(detail=False, methods=['get'], url_path='daily-sales', url_name='daily_sales')
    def daily_sales(self, request):
        daily_sales = SalesReport.objects.values('date').annotate(total_sales=Sum('total_sales')).order_by('-date')
        return Response(daily_sales)

