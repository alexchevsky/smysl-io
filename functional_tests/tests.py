from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from django.core.files import File
from django.test import LiveServerTestCase, Client
from blog.models import Article
from api.models import Task, Token
from django.contrib.auth import get_user_model

from datetime import datetime
import json
import pytz
import os
from time import sleep

from django.test.utils import override_settings
from django.urls import reverse
from django.conf import settings

import json

class BlogTests(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full_text 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='title-1',
            category='category-1',
            og_image=File(open('test_images/test_image_1.png', 'rb'))
        )
        Article.objects.create(
            title='title 2',
            summary='summary 2',
            full_text='full_text 2',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-2',
            category='category-1',
            og_image=File(open('test_images/test_image_1.png', 'rb'))
        )
        Article.objects.create(
            title='title 3',
            summary='summary 3',
            full_text='full_text 3',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-3',
            category='category-2',
            og_image=File(open('test_images/test_image_2.png', 'rb'))
        )

    def tearDown(self):
        self.browser.quit()

    #  TODO this test is incorrect
    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        footer = self.browser.find_element(By.CLASS_NAME, 'footer')
        self.assertTrue(footer.location['y'] > 500)

    def test_home_page_blog(self):
        # Под шапкой раположен блог со статьями.
        self.browser.get(self.live_server_url)
        article_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        # У каждой статьи есть заголовок и один абзац с текстом
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(
            By.CLASS_NAME,
            'article-title')
        article_text = self.browser.find_element(
            By.CLASS_NAME,
            'article-text')
        self.assertTrue(article_title)
        self.assertTrue(article_text)


    def test_home_page_article_title_link_leads_to_article_page(self):
        # Вася кликнул по заголовку и у него открылась страница
        # с полным текстом статьи
        self.browser.get(self.live_server_url)
        article = self.browser.find_element(
            By.CLASS_NAME,
            'article')
        article_title = article.find_element(
            By.CLASS_NAME,
            'article-title')
        article_title_text = article_title.text
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        href = article_link.get_attribute('href')
        self.browser.get(href)
        article_page_title = self.browser.find_element(
            By.CLASS_NAME,
            'article-title')
        self.assertEqual(article_title_text, article_page_title.text)

    def test_article_link_without_slash_works(self):
        # Вася случайно удалил / из ссылки, ведущей на статью,
        # но статья все равно открылась
        self.browser.get(self.live_server_url)
        article = self.browser.find_element(
            By.CLASS_NAME,
            'article')
        article_title = article.find_element(
            By.CLASS_NAME,
            'article-title')
        article_title_text = article_title.text
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        href = article_link.get_attribute('href')
        if href[-1] == '/':
            href = href[:-1]  # removing trailing slash
        self.browser.get(href)
        article_page_title = self.browser.find_element(By.CLASS_NAME,
                                                       'article-title')
        self.assertEqual(article_title_text, article_page_title.text)

    def test_article_page_header_has_link_that_leads_to_home(self):
        # На странице статьи Вася кликнул по заголовку в шапке сайта
        # и попал на главную страницу
        self.browser.get(self.live_server_url)
        initial_url = self.browser.current_url
        article = self.browser.find_element(
            By.CLASS_NAME,
            'article')
        article_title = article.find_element(
            By.CLASS_NAME,
            'article-title')
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        href = article_link.get_attribute('href')
        self.browser.get(href)
        page_header = self.browser.find_element(
            By.CLASS_NAME,
            'avatar-top')
        href_back = page_header.find_element(
            By.TAG_NAME, 'a').get_attribute('href')
        self.browser.get(href_back)
        final_url = self.browser.current_url
        self.assertEqual(initial_url, final_url)

    def test_python_landing_redirect(self):
        self.browser.get(self.live_server_url + '/python')
        self.assertIn('Python для маркетологов и продактов',
                      self.browser.title)

    def test_setup_landing_redirect(self):
        self.browser.get(self.live_server_url + '/setup')
        self.assertIn('Настройка Python для работы с данными',
                      self.browser.title)

    def test_dev_landing_redirect(self):
        self.browser.get(self.live_server_url + '/dev')
        self.assertIn('Рассылка о создании цифровых продуктов',
                      self.browser.title)

    def test_trello_landing_redirect(self):
        self.browser.get(self.live_server_url + '/trello')
        self.assertIn('Trello',
                      self.browser.title)

    def test_category_page_displays_correct_articles(self):
        self.browser.get(self.live_server_url)
        article = self.browser.find_element(
            By.CLASS_NAME,
            'article')
        article_footer = article.find_element(
            By.CLASS_NAME,
            'article-footer')
        category_link = article_footer.find_element(By.TAG_NAME, 'a')
        category = category_link.text
        self.browser.get(category_link.get_attribute('href'))
        page = self.browser.find_element(
            By.TAG_NAME,
            'body')
        self.assertIn(category, self.browser.title)
        self.assertIn(category, page.text)

class APIFunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server
        self.public_task = Task.objects.create(description="Public Task", is_public=True)
        self.private_task = Task.objects.create(description="Private Task", is_public=False)
        # Token.objects.create(email='user@example.com')
        self.valid_token = Token.objects.create(email="user@example.com")

    def tearDown(self):
        self.browser.quit()

    def test_health_endpoint(self):
        client = Client()
        response = client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status_code": 200, "message": "API is online"})
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_tasks_endpoint(self):
        client = Client()
        response = client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)  # Assuming 2 tasks for the test
        self.assertTrue(data[0]['is_public'])
        self.assertFalse(data[1]['is_public'])

    def test_public_task_access(self):
        client = Client()
        tasks = client.get('/tasks').json()
        response = self.client.get(f'/tasks/{tasks[0]["id"]}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['description'], "Public Task")

    def test_private_task_access(self):
        client = Client()
        tasks = client.get('/tasks').json()
        response = self.client.get(f'/tasks/{tasks[1]["id"]}')
        self.assertEqual(response.status_code, 403)

    def test_task_detail_with_valid_token(self):
        url = reverse('task_detail', args=[self.private_task.id])
        response = self.client.get(url, HTTP_AUTHORIZATION=self.valid_token.token)
        self.assertEqual(response.status_code, 200)


    def test_get_token_functional(self):
        client = Client()
        data = json.dumps({'email': 'user@example.com'})
        response = client.post(reverse('get_token'), data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertIn('api_token', response_data)
        self.assertIn('expires_at', response_data)

        # Ensure that the token is saved in the database
        self.assertTrue(Token.objects.filter(token=response_data['api_token']).exists())


class UserRegistrationLoginTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server
        self.public_task = Task.objects.create(description="Public Task", is_public=True)
        self.private_task = Task.objects.create(description="Private Task", is_public=False)
        # Token.objects.create(email='user@example.com')
        self.valid_token = Token.objects.create(email="user@example.com")

    def tearDown(self):
        self.browser.quit()
    
    def test_user_registration_and_login(self):
        # Navigate to the registration page
        self.browser.get(self.live_server_url + '/register/')  # Adjust the URL based on your site's URL pattern

        # Fill out the registration form
        email_input = self.browser.find_element_by_name('email') 
        email_input.send_keys('testuser@example.com')

        password_input = self.browser.find_element_by_name('password')  # Adjust the field name as necessary
        password_input.send_keys('password123')

        password_confirm_input = self.browser.find_element_by_name('password_confirm')  # Confirm password field
        password_confirm_input.send_keys('password123')

        submit_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()

        # Wait for the page to load
        sleep(1)

        # Navigate to the login page
        self.browser.get(self.live_server_url + '/login/')  # Adjust the URL based on your site's URL pattern

        # Fill out the login form
        email_input = self.browser.find_element_by_name('username')  # Changed from 'username' to 'email', if your login uses email
        email_input.send_keys('testuser@example.com')

        password_input = self.browser.find_element_by_name('password')  # Adjust the field name as necessary
        password_input.send_keys('password123')

        submit_button = self.browser.find_element_by_xpath("//button[@type='submit']")  # Changed from input to button
        submit_button.click()

        # Wait for response
        sleep(1)


class SecretPagesTests(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        # Create a test user
        User = get_user_model()
        User.objects.create_user(email='test@example.com', password='password123')

    def tearDown(self):
        self.browser.quit()

    def test_redirect_to_login_and_then_to_my_page(self):
        # Try to access the my page
        self.browser.get(self.live_server_url + reverse('my'))
        # Check for redirection to the login page
        self.assertIn("Login", self.browser.title)

        # Perform login
        email_input = self.browser.find_element_by_name('username')
        email_input.send_keys('test@example.com')
        password_input = self.browser.find_element_by_name('password')
        password_input.send_keys('password123')
        submit_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()

        # Assert redirection to the my page
        self.assertEqual(self.browser.current_url, self.live_server_url + reverse('my'))

    def test_redirect_to_login_and_then_to_profile_page(self):
        # Try to access the profile page
        self.browser.get(self.live_server_url + reverse('profile'))
        # Check for redirection to the login page and similar steps as above

class LogoutTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        User = get_user_model()
        User.objects.create_user(email='test@example.com', password='password123')
        self.browser.get(self.live_server_url + reverse('login'))

        # Perform login
        email_input = self.browser.find_element_by_name('username')  # Adjust based on your login form
        email_input.send_keys('test@example.com')
        password_input = self.browser.find_element_by_name('password')
        password_input.send_keys('password123')
        submit_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()

    def tearDown(self):
        self.browser.quit()

    def test_logout(self):
        # Navigate to logout link or button
        logout_link = self.browser.find_element_by_id('logout')  # Adjust the selector as per your logout link/button
        logout_link.click()

        # Check if redirected to login page or another specified page after logout
        try:
            self.browser.find_element_by_id('login')
        except NoSuchElementException:
            self.fail("Login link is not present on the page")  # Adjust based on your page title after logout

        # Optionally, attempt to access a protected page and check for redirection to login page
        self.browser.get(self.live_server_url + reverse('my'))
        self.assertIn("Login", self.browser.title)  # Adjust based on expected behavior
