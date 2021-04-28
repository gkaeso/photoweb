from django.test import TestCase, Client
from django.urls import reverse


class IndexText(TestCase):
    
    def test_page(self):
        response = self.client.get(reverse('website:index'))
        self.assertEqual(response.status_code, 200)