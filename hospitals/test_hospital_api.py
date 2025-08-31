from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import HospitalUser
from hospitals.models import ResourceStatus, TransferLog

class HospitalAPITests(APITestCase):

    def setUp(self):
        self.user = HospitalUser.objects.create_user(
            username="testuser",
            password="pass123",
            
        )
        self.client.login(username="testuser", password="pass123")

    def test_list_hospitals(self):
        response = self.client.get("/api/hospitals/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Hospital", str(response.data))

    def test_hospital_detail(self):
        response = self.client.get(f"/api/hospitals/{self.user.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Hospital")

class TransferAPITests(APITestCase):

    def setUp(self):
        self.h1 = HospitalUser.objects.create_user(
            username="hospitalA",
            password="pass123",
            
        )
        self.h2 = HospitalUser.objects.create_user(
            username="hospitalB",
            password="pass123",
            
        )
        self.user = self.h1
        self.client.login(username="hospitalA", password="pass123")

    def test_create_transfer(self):
        payload = {
            "patient_name": "John Doe",
            "from_hospital": self.h1.id,
            "to_hospital": self.h2.id,
            "reason": "Test transfer"
        }
        response = self.client.post("/api/transfers/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["patient_name"], "John Doe")