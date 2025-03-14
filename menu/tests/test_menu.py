import pytest
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from inventory.models import Inventory
from orders.models import OrderItem
from reservations.models import Reservation
from menu.models import MenuItem
from django.contrib.auth import get_user_model
from model_bakery import baker

User = get_user_model()

@pytest.mark.django_db
class TestRetriveInventory(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass')
        self.menu = baker.make('menu.MenuItem')
        
    def test_if_unauthenticated_user_returns_401(self):
        response = self.api_client.get('/api/menu/items/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_authenticated_user_can_get_menu_list(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get('/api/menu/items/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0

    def test_if_authenticated_user_can_get_menu_detail(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get(f'/api/menu/items/{self.menu.id}/')
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestCreateUpdateDeleteMenu(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass')
        self.superuser = User.objects.create_superuser(email='testsuperuser@gmail.com', password='testpass')
        self.menu = baker.make('menu.MenuItem')

    def test_if_authenticated_user_can_create_menu(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.post('/api/menu/items/', {
            'name': 'Test Item 2', 
            'description': 'Test Description',
            'price': 50.00,
            'category': 1,
            'available': True
            })
        assert response.status_code == status.HTTP_201_CREATED
        
    def test_if_is_not_authenticated_user_can_not_create_menu(self):
        response = self.api_client.post('/api/menu/items/', {
            'name': 'Test Item 2', 
            'description': 'Test Description',
            'price': 50.00,
            'category': 1,
            'available': True
            })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_not_superuser_can_not_create_menu(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.post('/api/menu/items/', {
            'name': 'Test Item 2', 
            'description': 'Test Description',
            'price': 50.00,
            'category': 1,
            'available': True
            })
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_authenticated_user_can_update_menu(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.put(f'/api/menu/items/{self.menu.id}/', {
            'name': 'Test Item 2', 
            'description': 'Test Description',
            'price': 50.00,
            'category': 1,
            'available': True
            })
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_is_not_authenticated_user_can_not_update_menu(self):
        response = self.api_client.put(f'/api/menu/items/{self.menu.id}/', {
            'name': 'Test Item 2', 
            'description': 'Test Description',
            'price': 50.00,
            'category': 1,
            'available': True
            })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_not_superuser_can_not_update_menu(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.put(f'/api/menu/items/{self.menu.id}/', {
            'name': 'Test Item 2', 
            'description': 'Test Description',
            'price': 50.00,
            'category': 1,
            'available': True
            })
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_authenticated_user_can_delete_menu(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.delete(f'/api/menu/items/{self.menu.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        
    
        
    def test_if_is_not_authenticated_user_can_not_delete_menu(self):
        response = self.api_client.delete(f'/api/menu/items/{self.menu.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_not_superuser_can_not_delete_menu(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.delete(f'/api/menu/items/{self.menu.id}/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

 