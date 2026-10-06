from unittest.mock import patch

from django.db import DatabaseError
from django.contrib.auth import get_user_model
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


class ServiceRequestAdminTests(TestCase):
    def test_admin_list_shows_request_description_preview(self):
        admin_user = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='test-password',
        )
        ServiceRequest.objects.create(
            name='Ada Yılmaz',
            email='ada@example.com',
            service=ServiceRequest.Service.WEBSITE,
            description='Kurumsal web sitesi için yeni bir tasarım talebi.',
        )
        self.client.force_login(admin_user)

        response = self.client.get(reverse('admin:requests_app_servicerequest_changelist'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kurumsal web sitesi için yeni bir tasarım talebi.')
