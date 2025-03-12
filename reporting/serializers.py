from rest_framework import serializers
from .models import InventoryReport
from .models import SalesReport

class InventoryReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = InventoryReport
        fields = ['date', 'item_name', 'quantity_used', 'quantity_remaining']


class SalesReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = SalesReport
        fields = ['date', 'total_sales', 'total_orders']

