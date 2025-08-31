from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import HospitalUser
from hospitals.models import ResourceStatus

class ResourceStatusAPITests(APITestCase):
    def setUp(self):
        self.hospital = HospitalUser.objects.create_user(
            username="hosp1", password="pass123", #name="Hospital 1", role="hospital_admin"
        )
        self.client.login(username="hosp1", password="pass123")

        self.resource_payload = {
            "hospital": self.hospital.id,
            "beds": 10,
            "icu_beds": 2,
            "oxygen_cylinders": 5,
            "available_doctors": 3
        }

    def test_create_resource_status(self):
        response = self.client.post("/api/resource-status/", self.resource_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ResourceStatus.objects.count(), 1)

    def test_list_resource_status(self):
        ResourceStatus.objects.create(
            hospital=self.hospital,
            beds=8,
            icu_beds=1,
            oxygen_cylinders=4,
            available_doctors=2
        )
        response = self.client.get("/api/resource-status/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # If paginated, use response.data['results'], else response.data
        statuses = response.data if isinstance(response.data, list) else response.data.get('results', [])
        self.assertGreaterEqual(len(statuses), 1)