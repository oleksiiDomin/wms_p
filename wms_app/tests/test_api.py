import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from wms_app.models import Seller
from wms_app.serializers import SellerSerializer



class SellerApiTestCase(APITestCase):


    def setUp(self):
        self.user = User.objects.create_user(username='test')
        self.seller1 = Seller.objects.create(name="test1", country="US", city="San Francisco")
        self.seller2 = Seller.objects.create(name="test2", country="Ukraine", city="Kiyv")
        self.seller3 = Seller.objects.create(name="test3", country="Ukraine", city="Dnipro")


    def test_get(self):
        url = reverse('seller-list')

        response = self.client.get(url)

        serializer_data = SellerSerializer([self.seller1, self.seller2, self.seller3], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)


    def test_get_search(self):
        url = reverse('seller-list')

        response = self.client.get(url, data={'search': 'Ukraine'})

        serializer_data = SellerSerializer([self.seller2, self.seller3], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)


    def test_post(self):
        url = reverse('seller-list')
        data = {'name': 'test1', 'country': 'US', 'city': 'San Francisco'}
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_put(self):
        url = reverse('seller-detail', args={self.seller1.id})
        data = {'name': self.seller1.name, 'country': self.seller1.country, 'city': 'New York'}
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.seller1.refresh_from_db()
        self.assertEqual('New York', self.seller1.city)