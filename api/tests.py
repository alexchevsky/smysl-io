from django.test import TestCase
from django.urls import reverse

class HealthEndpointUnitTest(TestCase):
    def test_health_view_status_code(self):
        url = reverse('health')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status_code": 200, "message": "API is online"})
        self.assertEqual(response['Content-Type'], 'application/json')
