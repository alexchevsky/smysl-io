from django.test import TestCase
from django.urls import reverse
from datetime import datetime, timedelta
from .models import Task, Token
from django.utils import timezone
from datetime import timedelta

class HealthEndpointUnitTest(TestCase):
    def test_health_view_status_code(self):
        url = reverse('health')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status_code": 200, "message": "API is online"})
        self.assertEqual(response['Content-Type'], 'application/json')

class TasksEndpointUnitTest(TestCase):
    def test_tasks_view(self):
        Task.objects.create(
            is_public=True,
            description='full_text 1',
        )
        Task.objects.create(
            is_public=False,
            description='full_text 2',
        )

        url = reverse('tasks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertTrue(len(data)>=2)
        self.assertTrue(list(data[0].keys()) == ['id', 'is_public'])

class TaskDetailViewTests(TestCase):
    def setUp(self):
        self.public_task = Task.objects.create(description="Public Task", is_public=True)
        self.private_task = Task.objects.create(description="Private Task", is_public=False)
        self.valid_token = Token.objects.create(email="user@example.com")
        self.expired_token = Token.objects.create(email="expired@example.com", expires_at=timezone.now() - timedelta(days=1))
    
    def test_access_with_valid_token(self):
        url = reverse('task_detail', args=[self.private_task.id])
        response = self.client.get(url, HTTP_AUTHORIZATION=self.valid_token.token)
        self.assertEqual(response.status_code, 200)

    def test_access_with_expired_token(self):
        url = reverse('task_detail', args=[self.private_task.id])
        response = self.client.get(url, HTTP_AUTHORIZATION=self.expired_token.token)
        self.assertEqual(response.status_code, 403)

    def test_access_with_invalid_token(self):
        url = reverse('task_detail', args=[self.private_task.id])
        response = self.client.get(url, HTTP_AUTHORIZATION='invalidtoken')
        self.assertEqual(response.status_code, 403)

    def test_public_task_detail(self):
        url = reverse('task_detail', args=[self.public_task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'id': self.public_task.id,
            'description': 'Public Task',
            'is_public': True
        })

    def test_access_without_token(self):
        url = reverse('task_detail', args=[self.private_task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_nonexistent_task_detail(self):
        url = reverse('task_detail', args=[999])  # Assuming this ID does not exist
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

class TaskModelUnitTest(TestCase):

    def test_task_model_save_and_retrieve(self):

        task1 = Task(
            is_public=True,
            description='full_text 1',
        )
        task1.save()

        task2 = Task(
            is_public=False,
            description='full_text 2',
        )
        task2.save()

        all_tasks = Task.objects.all()

        self.assertEqual(len(all_tasks), 2)

        self.assertEqual(
            all_tasks[0].is_public,
            task1.is_public
        )
        self.assertEqual(
           all_tasks[0].description,
            task1.description
        )

        self.assertEqual(
            all_tasks[1].is_public,
            task2.is_public
        )
        self.assertEqual(
            all_tasks[1].description,
            task2.description
        )


class GetTokenTests(TestCase):
    def test_get_token_success(self):
        response = self.client.post(reverse('get_token'), {'email': 'test@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('api_token', response.json())
        self.assertIn('expires_at', response.json())

        token = response.json()['api_token']
        self.assertTrue(Token.objects.filter(token=token).exists())

    def test_get_token_no_email(self):
        response = self.client.post(reverse('get_token'))
        self.assertEqual(response.status_code, 400)


class TaskModelTokenTest(TestCase):

    def test_token_model_save_and_retrieve(self):

        token = Token(
            email='user@example.com'
        )
        token.save()

        all_tokens = Token.objects.all()
        self.assertEqual(len(all_tokens), 1)

        self.assertEqual(
            all_tokens[0].email,
            token.email
        )