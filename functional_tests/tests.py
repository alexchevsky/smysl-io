from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from blog.models import Article
from django.urls import reverse
from datetime import datetime
import pytz
import os

class BlogTests(LiveServerTestCase):
# Жил был Вася
# Вася работает аналитиком в какой-то компании
# Однажды Вася захотел прокачаться в когортном анализе
# Вася зашел в Гугл, ввел запрос "Когортный анализ" и кликнул по одной из ссылок


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
            slug='ooo-lya-lya'
        )

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        # В браузере Васи открылся сайт (по адресу http://127.0.0.1:8000)
        # В заголовке сайта Вася прочитал "Сайт Алексея Куличевского"
        self.browser.get(self.live_server_url)
        self.assertIn('Сайт Алексея Куличевского', self.browser.title)

    def test_home_page_header(self):
        # В шапке сайта написано "Алексей Куличевский"
        self.browser.get(self.live_server_url)
        header = self.browser.find_element(By.CLASS_NAME, 'avatar-top')
        self.assertIn('Алексей Куличевский', header.text)

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

    def find_href_to_article(self):
        article_title = self.browser.find_element(
            By.CLASS_NAME,
            'article-title')
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        return article_link.get_attribute('href')

    def test_home_page_article_title_link_leads_to_article_page(self):
        # Вася кликнул по заголовку и у него открылась страница
        # с полным текстом статьи
        self.browser.get(self.live_server_url)
        article_title_text = self.browser.find_element(
            By.CLASS_NAME,
            'article-title').text
        href = self.find_href_to_article()
        self.browser.get(href)
        article_page_title = self.browser.find_element(
            By.CLASS_NAME,
            'article-title')
        self.assertEqual(article_title_text, article_page_title.text)

    def test_article_link_without_slash_works(self):
        # Вася случайно удалил / из ссылки, ведущей на статью,
        # но статья все равно открылась
        self.browser.get(self.live_server_url)
        article_title_text = self.browser.find_element(
            By.CLASS_NAME,
            'article-title').text
        href = self.find_href_to_article()
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
        href = self.find_href_to_article()
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




# self.fail('Finish the test!')



# На странице статьи Вася прочитал заголовок страницы: там был написан заголовок статьи

# Вася попытался открыть несуществующую статью и ему открылась
# Красивая страничка "Страница не найдена"

# Прочитал статью Вася кликнул по тексту "Алексей Куличевский" в шапке сайта и 
# попал обратно на главную страницу.

# Некоторые статьи есть в админке, но они не опубликованы