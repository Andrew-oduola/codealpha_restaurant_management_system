from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        data = request.data
        table_id = data.get('table')
        items_data = data.get('items')

        if not table_id or not items_data:
            return Response(
                {'error': 'Please provide table and items data'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create the order
        order = Order.objects.create(table_id=table_id)

        # Prepare OrderItem objects for bulk_create
        order_items = []
        for item in items_data:
            try:
                order_items.append(OrderItem(
                    order=order,
                    menu_item_id=item['menu_item'],
                    quantity=item['quantity']
                ))
            except KeyError as e:
                return Response(
                    {'error': f'Missing key in items data: {str(e)}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        OrderItem.objects.bulk_create(order_items)  # Efficient batch insert

        # Calculate total price using OrderItem (not order.items.all())
        total_price = sum(item.menu_item.price * item.quantity for item in OrderItem.objects.filter(order=order))
        order.total_price = total_price
        order.save()

        # Serialize response
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
