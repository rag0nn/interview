from unittest.mock import patch

from django.db import DatabaseError
from django.test import TestCase
from django.urls import reverse

from .models import ServiceRequest


class ServiceRequestSubmissionTests(TestCase):
    def setUp(self):
        self.url = reverse('requests_app:home')
        self.valid_data = {
            'name': 'Ada Yılmaz',
            'email': 'ada@example.com',
            'service': ServiceRequest.Service.WEBSITE,
            'description': 'Kurumsal web sitem için yeni bir tasarım istiyorum.',
        }

    def test_valid_submission_is_saved_before_success_redirect(self):
        response = self.client.post(self.url, self.valid_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Talebiniz ulaştı.')
        self.assertEqual(ServiceRequest.objects.count(), 1)

    def test_invalid_submission_is_not_saved(self):
        response = self.client.post(self.url, {**self.valid_data, 'email': 'invalid'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'E-posta')
        self.assertEqual(ServiceRequest.objects.count(), 0)

    @patch('requests_app.views.ServiceRequestForm.save', side_effect=DatabaseError)
    def test_database_error_shows_error_without_success(self, save_request):
        with self.assertLogs('requests_app.views', level='ERROR'):
            response = self.client.post(self.url, self.valid_data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Talebiniz şu anda kaydedilemedi.')
        self.assertNotContains(response, 'Talebiniz ulaştı.')
        self.assertEqual(ServiceRequest.objects.count(), 0)
