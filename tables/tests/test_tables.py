import pytest
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from model_bakery import baker
from tables.models import Table

User = get_user_model()

@pytest.mark.django_db
class TestRetriveTables(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email="testuser@gmail.com", password="testpassword234")
        self.table = baker.make(Table)
    
    def test_if_unauthenticated_user_returns_401_table(self):
        response = self.api_client.get('/api/tables/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_authenticated_user_can_get_tables_list(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get('/api/tables/')
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_authenticated_user_can_get_table_detial(self):
        self.api_client.force_authenticate(user=self.user)
        response =  self.api_client.get(f'/api/tables/{self.table.id}/')
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_unauthenticated_user_can_not_get_table_detial(self):
        response =  self.api_client.get(f'/api/tables/{self.table.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
        
@pytest.mark.django_db
class TestCreateUpdateDeleteTable(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testuserpassword')
        self.superuser = User.objects.create_superuser(email='testsuperuser@gmail.com', password='testsuperuserpassword')
        self.table = baker.make(Table)
        
    def test_if_authenticated_user_can_create_tables(self):
        self.api_client.force_authenticate(user=self.user) 
        response = self.api_client.post('/api/tables/', {
            "table_number": 420,
            "capacity": 638,
            "is_occupied": True,
            "location": "Delectus accusamus consequatur.",
            "seats": 181
        })
        assert response.status_code == status.HTTP_201_CREATED
        
    def test_if_unauthenticated_user_cannot_create_tables(self):
        response = self.api_client.post('/api/tables/', {
            "table_number": 420,
            "capacity": 638,
            "is_occupied": True,
            "location": "Delectus accusamus consequatur.",
            "seats": 181
        })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_authenticated_user_can_update_tables(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.put(f'/api/tables/{self.table.id}/', {
            "table_number": 420,
            "capacity": 638,
            "is_occupied": True,
            "location": "Delectus accusamus consequatur.",
            "seats": 181
            })
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_is_not_authenticated_user_can_not_update_tables(self):
        response = self.api_client.put(f'/api/tables/{self.table.id}/', {
            "table_number": 420,
            "capacity": 638,
            "is_occupied": True,
            "location": "Delectus accusamus consequatur.",
            "seats": 181
            })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
     

    def test_if_authenticated_user_can_delete_tables(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.delete(f'/api/tables/{self.table.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        
    
    def test_if_is_not_authenticated_user_can_not_delete_table(self):
        response = self.api_client.delete(f'/api/tables/{self.table.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        