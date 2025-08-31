from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTests(APITestCase):

    def setUp(self):
        self.register_url = reverse("register")  # replace with your actual name
        self.login_url = reverse("token_obtain_pair")
        self.user_data = {
            "email": "testuser@example.com",
            "password": "securepassword123"
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_user_registration(self):
        response = self.client.post(self.register_url, {
            "email": "newuser@example.com",
            "password": "newpassword123"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("email", response.data)

    def test_user_login(self):
        response = self.client.post(self.login_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
