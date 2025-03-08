from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        table_id = data.get('table')
        items_data = data.get('items')

        # Create the order
        order = Order.objects.create(table_id=table_id)

        # Add order items
        for item_data in items_data:
            OrderItem.objects.create(
                order=order,
                menu_item_id=item_data['menu_item'],
                quantity=item_data['quantity']
            )

        # Calculate total price
        total_price = sum(item.menu_item.price * item.quantity for item in order.items.all())
        order.total_price = total_price
        order.save()

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer