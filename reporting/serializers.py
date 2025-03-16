from rest_framework import serializers
from .models import InventoryReport
from .models import SalesReport

class InventoryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryReport
        fields = ['id', 'date', 'item_name', 'quantity_used', 'quantity_remaining']


class SalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReport
        fields = ['id', 'date', 'total_sales', 'total_orders']

