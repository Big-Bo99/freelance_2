from django.test import Client
from rest_framework import status

from rest_framework.test import APITestCase


class TestUserCreation(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create a new user(executor) object.
        """
        url = 'http://127.0.0.1:8000/api/v1/customers/'
        data = {
            "name": "test",
            "first_name": "test",
            "last_name": "test",
            "username": "test1",
            "email": "test@gmail.com",
            "balance": "10"
            }
        client = Client()
        response = client.post(url, data)
        print(response.status_code)
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
