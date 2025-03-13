import pytest
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from inventory.models import Inventory
from orders.models import OrderItem
from reservations.models import Reservation
from django.contrib.auth import get_user_model
from model_bakery import baker

User = get_user_model()

@pytest.mark.django_db
class TestRetriveInventory(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass')
        
        self.inventory = Inventory.objects.create(item_name="Test Item", quantity=5, reorder_level=10)
        
    def test_if_unauthenticated_user_returns_401(self):
        response = self.api_client.get('/api/inventory/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_authenticated_user_can_get_inventory_list(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get('/api/inventory/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0

    def test_if_authenticated_user_can_get_low_stock_inventory_list(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get('/api/inventory/low-stock/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_authenticated_user_can_get_inventory_detail(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get(f'/api/inventory/{self.inventory.id}/')
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestCreateUpdateDeleteInventory(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass')
        self.inventory = Inventory.objects.create(item_name="Test Item", quantity=5, reorder_level=10)
        
    def test_if_authenticated_user_can_create_inventory(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.post('/api/inventory/', {
            'item_name': 'Test Item 2', 
            'quantity': 10, 
            'reorder_level': 5,
            'unit': 50.00
            })
        assert response.status_code == status.HTTP_201_CREATED

    def test_if_authenticated_user_can_update_inventory(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.put(f'/api/inventory/{self.inventory.id}/', {
            'item_name': 'Test Item 2', 
            'quantity': 10, 
            'reorder_level': 5,
            'unit': 50.00
            })
        assert response.status_code == status.HTTP_200_OK

    def test_if_authenticated_user_can_delete_inventory(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.delete(f'/api/inventory/{self.inventory.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT

@pytest.mark.django_db
class TestInventoryModel:
    def test_inventory_model(self):
        inventory = baker.make('inventory.Inventory')
        assert isinstance(inventory, Inventory)
        assert inventory.__str__() == inventory.item_name
