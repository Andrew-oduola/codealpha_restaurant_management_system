import pytest
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from model_bakery import baker
from reservations.models import Reservation

User = get_user_model()

@pytest.mark.django_db
class TestRetriveResevations(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email="testuser@gmail.com", password="testpassword234")
        self.reservation = baker.make(Reservation)
    
    def test_if_unauthenticated_user_returns_401_reservations(self):
        response = self.api_client.get('/api/reservations/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_authenticated_user_can_get_reservations_list(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get('/api/reservations/')
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_authenticated_user_can_get_reservation_detial(self):
        self.api_client.force_authenticate(user=self.user)
        response =  self.api_client.get(f'/api/reservations/{self.reservation.id}/')
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_unauthenticated_user_can_not_get_reservation_detial(self):
        response =  self.api_client.get(f'/api/reservations/{self.reservation.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
        
@pytest.mark.django_db
class TestCreateUpdateDeleteReservation(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testuserpassword')
        self.superuser = User.objects.create_superuser(email='testsuperuser@gmail.com', password='testsuperuserpassword')
        self.reservation = baker.make(Reservation)
        
    def test_if_authenticated_user_can_create_reservation(self):
        self.api_client.force_authenticate(user=self.user) 
        response = self.api_client.post('/api/reservations/', {
            "customer_name": "Johathan Mitchell",
            "customer_contact": "China",
            "reservation_time": "2024-03-17T14:23:00Z",
            "party_size": 46,
            "special_requests": "36165 Rhea Trace",
            "table": 1
        })
        assert response.status_code == status.HTTP_201_CREATED
        
    def test_if_unauthenticated_user_cannot_create_reservation(self):
        response = self.api_client.post('/api/reservations/', {
            "customer_name": "Johathan Mitchell",
            "customer_contact": "China",
            "reservation_time": "2024-03-17T14:23:00Z",
            "party_size": 46,
            "special_requests": "36165 Rhea Trace",
            "table": 1
        })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_authenticated_user_can_update_reservation(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.put(f'/api/reservations/{self.reservation.id}/', {
            "customer_name": "Johathan Mitchell",
            "customer_contact": "China",
            "reservation_time": "2024-03-17T14:23:00Z",
            "party_size": 46,
            "special_requests": "36165 Rhea Trace",
            "table": 1
            })
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_is_not_authenticated_user_can_not_update_reservation(self):
        response = self.api_client.put(f'/api/reservations/{self.reservation.id}/', {
            "customer_name": "Johathan Mitchell",
            "customer_contact": "China",
            "reservation_time": "2024-03-17T14:23:00Z",
            "party_size": 46,
            "special_requests": "36165 Rhea Trace",
            "table": 1
            })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
     

    def test_if_authenticated_user_can_delete_inventory(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.delete(f'/api/reservations/{self.reservation.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        
    
    def test_if_is_not_authenticated_user_can_not_delete_inventory(self):
        response = self.api_client.delete(f'/api/reservations/{self.reservation.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        