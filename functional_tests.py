from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class BasicInstallTest(unittest.TestCase):  
# Жил был Вася
# Вася работает аналитиком в какой-то компании
# Однажды Вася захотел прокачаться в когортном анализе
# Вася зашел в Гугл, ввел запрос "Когортный анализ" и кликнул по одной из ссылок

    def setUp(self):  
        self.browser = webdriver.Chrome()

    def tearDown(self):  
        self.browser.quit()

    def test_home_page_title(self):
        # В браузере Васи открылся сайт (по адресу http://127.0.0.1:8000)
        # В заголовке сайта Вася прочитал "Сайт Алексея Куличевского"
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Сайт Алексея Куличевского', self.browser.title)

    def test_home_page_header(self):
        # В шапке сайта написано "Алексей Куличевский"
        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Алексей Куличевский', header.text)

    def test_home_page_blog(self):
        # Под шапкой раположен блог со статьями.
        self.browser.get('http://127.0.0.1:8000')
        article_list = self.browser.find_element_by_class_name('article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        # У каждой статьи есть заголовок и один абзац с текстом
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element_by_class_name(
            'article-title')
        article_summary = self.browser.find_element_by_class_name(
            'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)


if __name__ == '__main__':
    unittest.main()

# self.fail('Finish the test!')






# Вася кликнул по заголовку и у него открылась страница с полным текстом статьи

# Прочитал статью Вася кликнул по тексту "Алексей Куличевский" в шапке сайта и 
# попал обратно на главную страницу.
