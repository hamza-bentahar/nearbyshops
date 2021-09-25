from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase


class ShopTest(APITestCase):
    fixtures = ['shops_list.json']

    def test_get_shop_list(self):
        response = self.client.get(reverse('shop-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_shop_details(self):
        response = self.client.get(reverse('shop-detail', kwargs={'pk': 1}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
