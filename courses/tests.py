from django.test import TestCase
from django.urls import reverse

class RedirectsTest(TestCase):

    def test_python_redirect(self):
        url = reverse('python_redirect')
        response = self.client.get(url)
        self.assertRedirects(response,
                             'https://mailchi.mp/cca4513bb958/ddlvgo33yv/',
                             fetch_redirect_response=False)

    def test_setup_redirect(self):
        url = reverse('setup_redirect')
        response = self.client.get(url)
        self.assertRedirects(response,
                             'https://mailchi.mp/d823cd1db54d/python/',
                             fetch_redirect_response=False)
