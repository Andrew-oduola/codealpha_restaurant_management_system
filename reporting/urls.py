from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import SalesReportViewSet, InventoryReportViewSet


router = DefaultRouter()
router.register(r'inventory', InventoryReportViewSet)
router.register(r'sales', SalesReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]