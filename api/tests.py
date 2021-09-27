from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase


class AuthenticationTest(APITestCase):
    def test_registration(self):
        data = {
            "username": "test1",
            "email": "test1@email.com",
            "first_name": "hello",
            "last_name": "world",
            "password": "password123-",
            "password_confirmation": "password123-",
        }
        response = self.client.post(reverse('register-view'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data,
                         {'username': 'test1', 'email': 'test1@email.com', 'first_name': 'hello', 'last_name': 'world'})


class ShopTest(APITestCase):
    fixtures = ['shops_list.json']

    def test_get_shop_list(self):
        response = self.client.get(reverse('shop-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_shop_details(self):
        response = self.client.get(reverse('shop-detail', kwargs={'pk': 1}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LikedShopsTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@doe.com', 'password123-')
        self.client.login(username='john', password='password123-')

    def test_get_liked_shops(self):
        response = self.client.get(reverse('liked-shops'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
