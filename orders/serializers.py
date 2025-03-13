from rest_framework import serializers
from .models import Order, OrderItem
# from menu.models import MenuItem

# class MenuItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MenuItem
#         fields = ['name']


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source="orderitem_set", many=True)

    class Meta:
        model = Order
        fields = ['id', 'table', 'items', 'order_time', 'status', 'total_price', 'special_requests', 'status']
        read_only_fields = ['id', 'order_time', 'total_price']

    def create(self, validated_data):
        items_data = validated_data.pop('orderitem_set')  # Match the source name
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

