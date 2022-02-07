from selenium import webdriver
from django.core.files import File
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from blog.models import Article
from datetime import datetime
import pytz
import os
from time import sleep

from django.test.utils import override_settings
from django.conf import settings

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



# self.fail('Finish the test!')



# На странице статьи Вася прочитал заголовок страницы: там был написан заголовок статьи

# Вася попытался открыть несуществующую статью и ему открылась
# Красивая страничка "Страница не найдена"


# Некоторые статьи есть в админке, но они не опубликованы