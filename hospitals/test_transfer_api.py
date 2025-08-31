from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import HospitalUser
from hospitals.models import TransferLog

class TransferAPITests(APITestCase):
    def setUp(self):
        self.hospital1 = HospitalUser.objects.create_user(
            username="hosp1", password="pass123", ###name="Hospital 1", role="hospital_admin"
        )
        self.hospital2 = HospitalUser.objects.create_user(
            username="hosp2", password="pass123",# name="Hospital 2", role="hospital_admin"
        )

        self.client.login(username="hosp1", password="pass123")

        self.transfer_payload = {
            "patient_name": "John Doe",
            "from_hospital": self.hospital1.id,
            "to_hospital": self.hospital2.id,
            "reason": "Need specialist care"
        }

    def test_create_transfer(self):
        response = self.client.post("/api/transfers/", self.transfer_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TransferLog.objects.count(), 1)

    def test_list_transfers(self):
        TransferLog.objects.create(
            patient_name="Jane Doe",
            from_hospital=self.hospital1,
            to_hospital=self.hospital2,
            transferred_by=self.hospital1,
            reason="Emergency case"
        )
        response = self.client.get("/api/transfers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # If paginated, use response.data['results'], else response.data
        transfers = response.data if isinstance(response.data, list) else response.data.get('results', [])
        self.assertGreaterEqual(len(transfers), 1)