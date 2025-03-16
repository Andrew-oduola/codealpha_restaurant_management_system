import pytest
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from model_bakery import baker

from reporting.models import SalesReport, InventoryReport

User = get_user_model()

@pytest.mark.django_db
class TestRetriveReports(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass')
        self.salesreport = baker.make('reporting.SalesReport')
        self.inventoryreport = baker.make('reporting.InventoryReport')
        
    def test_if_unauthenticated_user_returns_401_inventory_reports(self):
        response = self.api_client.get('/api/reports/inventory/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_unauthenticated_user_returns_401_sales_reports(self):
        response = self.api_client.get('/api/reports/sales/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_authenticated_user_can_get_inventory_reports(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get('/api/reports/inventory/')
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_authenticated_user_can_get_sales_reports(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get('/api/reports/sales/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_authenticated_user_can_get_inventory_reports_detial(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get(f'/api/reports/inventory/{self.inventoryreport.id}/')
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_authenticated_user_can_get_sales_reports_detial(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get(f'/api/reports/sales/{self.salesreport.id}/')
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestCreateUpdateDeleteInventory(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass')
        self.superuser = User.objects.create_superuser(email='testsuperuser@gmail.com', password='testpass')
        self.inventoryreport = baker.make('reporting.InventoryReport')
        self.salesreport = baker.make('reporting.SalesReport')

    def test_if_authenticated_user_can_create_inventory_report(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.post('/api/reports/inventory/', {
            "date": "2024-12-15",
            "item_name": "Cletus Block",
            "quantity_used": 478,
            "quantity_remaining": 475
            })
        assert response.status_code == status.HTTP_201_CREATED
        
    def test_if_is_not_authenticated_user_can_not_create_inventory_report(self):
        response = self.api_client.post('/api/reports/inventory/', {
            "date": "2024-12-15",
            "item_name": "Cletus Block",
            "quantity_used": 478,
            "quantity_remaining": 475
            })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        

    def test_if_authenticated_user_can_update_inventory_report(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.put(f'/api/reports/inventory/{self.inventoryreport.id}/', {
            "date": "2024-12-15",
            "item_name": "Cletus Block",
            "quantity_used": 478,
            "quantity_remaining": 475
            })
        assert response.status_code == status.HTTP_200_OK
        
        
    def test_if_is_not_authenticated_user_can_not_update_inventory(self):
        response = self.api_client.put(f'/api/reports/inventory/{self.inventoryreport.id}/', {
            "item_name": "Cletus Block",
            "quantity_used": 478,
            "quantity_remaining": 475
            })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
     

    def test_if_authenticated_user_can_delete_inventory(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.delete(f'/api/reports/inventory/{self.inventoryreport.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        
    
    def test_if_is_not_authenticated_user_can_not_delete_inventory(self):
        response = self.api_client.delete(f'/api/reports/inventory/{self.inventoryreport.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        

@pytest.mark.django_db
class TestCreateUpdateDeleteSales(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass')
        self.superuser = User.objects.create_superuser(email='testsuperuser@gmail.com', password='testpass')
        self.inventoryreport = baker.make('reporting.InventoryReport')
        self.salesreport = baker.make('reporting.SalesReport')

    def test_if_authenticated_user_can_create_sales_report(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.post('/api/reports/sales/', {
            "date": "2024-07-17",
            "total_sales": "33332.00",
            "total_orders": 447
            })
        assert response.status_code == status.HTTP_201_CREATED
        
    def test_if_is_not_authenticated_user_can_not_create_inventory_report(self):
        response = self.api_client.post('/api/reports/sales/', {
            "date": "2024-07-17",
            "total_sales": "33332.00",
            "total_orders": 447
            })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        

    def test_if_authenticated_user_can_update_inventory_report(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.put(f'/api/reports/sales/{self.salesreport.id}/', {
            "date": "2024-07-17",
            "total_sales": "33332.00",
            "total_orders": 447
            })
        assert response.status_code == status.HTTP_200_OK
        
        
    def test_if_is_not_authenticated_user_can_not_update_inventory(self):
        response = self.api_client.put(f'/api/reports/sales/{self.salesreport.id}/', {
            "date": "2024-07-17",
            "total_sales": "33332.00",
            "total_orders": 447
            })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
     

    def test_if_authenticated_user_can_delete_inventory(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.delete(f'/api/reports/sales/{self.salesreport.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        
    
    def test_if_is_not_authenticated_user_can_not_delete_inventory(self):
        response = self.api_client.delete(f'/api/reports/sales/{self.salesreport.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
