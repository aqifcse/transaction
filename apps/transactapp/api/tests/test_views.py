from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class TransactionAPITest(APITestCase):
    
    def test_transaction_post(self):
        sample_transaction_data = {
            "sent_from": 2,
            "sent_to":[
                3,
                4
            ], 
            "sent_at": "2022-07-03T08:53:05Z",
            "amount_sent": 580.34  
        }

        response = self.client.post(reverse('transactapp:transaction'), sample_transaction_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)