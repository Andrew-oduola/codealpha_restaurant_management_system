from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MenuItemSerializer, MenuCategorySerializer
from .models import MenuItem, MenuCategory
from .permissions import IsAdminOrReadOnly

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'available', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name']
    ordering = ['name']  # Default ordering

    @action(detail=False, methods=['get'], url_path='available', url_name='available')
    def available_menu(self, request):
        available_items = MenuItem.objects.filter(available=True)
        serializer = self.get_serializer(available_items, many=True)
        return Response(serializer.data)

class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    # permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name']
    ordering = ['name']  # Default ordering
