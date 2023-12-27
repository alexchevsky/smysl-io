from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.sessions.middleware import SessionMiddleware
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser

User = get_user_model()

class CustomUserModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'testpass123'
        user = User.objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@EXAMPLE.COM'
        user = User.objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(None, 'test123')

    def test_create_superuser(self):
        user = User.objects.create_superuser('super@example.com', 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

class LoginViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user for testing login with the custom user model
        cls.user = User.objects.create_user(email='testuser@example.com', password='password123')

    def test_login_view_status_code(self):
        # Test that the login page is accessible
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_with_valid_credentials(self):
        # Test logging in with valid credentials
        response = self.client.post(reverse('login'), {'email': 'testuser@example.com', 'password': 'password123'})
        user = authenticate(email='testuser@example.com', password='password123')
        self.assertTrue(user is not None and user.is_authenticated)

    def test_login_with_invalid_credentials(self):
        # Test logging in with invalid credentials
        response = self.client.post(reverse('login'), {'email': 'testuser@example.com', 'password': 'wrongpassword'})
        user = authenticate(email='testuser@example.com', password='wrongpassword')
        self.assertFalse(user is not None and user.is_authenticated)

class RestrictedPageTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(email='user@example.com', password='password123')

    def test_my_page_redirects_unauthenticated_user(self):
        response = self.client.get(reverse('my'), follow=True)
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('my')}")

    def test_profile_page_redirects_unauthenticated_user(self):
        response = self.client.get(reverse('profile'), follow=True)
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('profile')}")

    def test_redirection_to_my_after_login(self):
        self.client.login(email='user@example.com', password='password123')
        response = self.client.get(reverse('my'))
        self.assertEqual(response.status_code, 200)

    def test_redirection_to_profile_after_login(self):
        self.client.login(email='user@example.com', password='password123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

class LogoutTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(email='test@example.com', password='password123')
        self.client.login(email='test@example.com', password='password123')

    def test_logout(self):
        # Perform logout
        response = self.client.get(reverse('logout'))

        # Check if the user is redirected to the appropriate page after logout
        self.assertRedirects(response, reverse('home_page'))  # Adjust as per your redirection URL

        # Check if the user is now anonymous (not logged in)
        user = self.client.get(reverse('home_page')).context['user']  # Assuming 'home' is a view accessible to logged-out users
        self.assertTrue(isinstance(user, AnonymousUser))