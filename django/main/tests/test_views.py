from django.test import TestCase
from django.urls import reverse

from main import forms


class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'main/home.html')
        self.assertContains(response, 'BookTime')

    def test_about_us_page_works(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'main/about_us.html')
        self.assertContains(response, 'BookTime')

    def test_contact_us_page_works(self):
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contact_form.html')
        self.assertContains(response, 'BookTime')
        self.assertIsInstance(
            response.context['form'], forms.ContactForm
        )