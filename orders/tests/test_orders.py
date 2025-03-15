import pytest
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from orders.models import OrderItem
from django.contrib.auth import get_user_model
from model_bakery import baker

User = get_user_model()

@pytest.mark.django_db
class TestRetrieveOrders(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass')
        self.order = baker.make('orders.Order')
        
    def test_if_unauthenticated_user_returns_401(self):
        response = self.api_client.get('/api/orders/orders/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_authenticated_user_can_get_order_list(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get('/api/orders/orders/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0

    def test_if_authenticated_user_can_get_order_detail(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get(f'/api/orders/orders/{self.order.id}/')
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestCreateUpdateDeleteOrders(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass')
        self.superuser = User.objects.create_superuser(email='testsuperuser@gmail.com', password='testpass')
        self.table = baker.make('tables.Table')
        self.menu_item = baker.make('menu.MenuItem')
        self.order = baker.make('orders.Order')

    # def test_if_authenticated_user_can_create_orders(self):
    #     self.api_client.force_authenticate(user=self.superuser)
    #     # print(self.menu_item.id)
    #     # print(self.table.id)
    #     response = self.api_client.post('/api/orders/orders/', {
    #         "table": self.table.id, 
    #         "items":  [
    #             {
    #                 "quantity": 2,
    #                 "menu_item": self.menu_item.id
    #             },
    #             {
    #                 "quantity": 1,
    #                 "menu_item": self.menu_item.id
    #             }
    #         ],
    #         "status": "pending",
    #         "special_requests": "Test Request"
    #     })
    #     assert response.status_code == status.HTTP_201_CREATED
    #     assert 'id' in response.data
    #     assert response.data['table'] == self.table.id
    #     assert len(response.data['items']) == 2
    #     assert response.data['status'] == "pending"
    #     assert response.data['special_requests'] == "Test Request"
        
    def test_if_authenticated_user_can_update_order(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.put(f'/api/orders/orders/{self.order.id}',
                                       {
                                          "special_requests": "Test 2 Request" 
                                       })

