from django.core.files import File
from django.test import TestCase
from blog.views import home_page, article_page
from blog.models import Article
from django.http import HttpRequest
from django.urls import reverse
from datetime import datetime
import pytz


class CategoriesPageTest(TestCase):
    def test_categories_page_displays_correct_articles(self):
        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full_text 1',
            category='category-1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-1',
            og_image=File(open('test_images/test_image_1.png', 'rb'))
        )
        Article.objects.create(
            title='title 2',
            summary='summary 2',
            full_text='full_text 2',
            category='category-1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-2',
            og_image=File(open('test_images/test_image_1.png', 'rb'))
        )
        Article.objects.create(
            title='title 3',
            summary='summary 3',
            full_text='full_text 3',
            category='category-2',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-3',
            og_image=File(open('test_images/test_image_1.png', 'rb'))
        )

        url = reverse('category_page', kwargs={'category': 'category-1'})
        response = self.client.get(url)
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertIn('title 2', html)
        self.assertNotIn('title 3', html)


class ArticlePageTest(TestCase):

    def test_article_page_displays_correct_article(self):
        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full_text 1',
            category='category-1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-1',
            og_image=File(open('test_images/test_image_1.png', 'rb'))
        )

        url = reverse('article_page', kwargs={'slug': 'slug-1'})
        response = self.client.get(url)
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertIn('full_text 1', html)
        self.assertNotIn('summary 1', html)


class HomePageTest(TestCase):

    def test_home_page_displays_articles(self):
        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full_text 1',
            category='category-1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-1',
            og_image=File(open('test_images/test_image_1.png', 'rb'))
        )
        Article.objects.create(
            title='title 2',
            summary='summary 2',
            full_text='full_text 2',
            category='category-1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-2',
            og_image=File(open('test_images/test_image_1.png', 'rb'))
        )

        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertIn('/blog/slug-1', html)
        self.assertNotIn('summary 1', html)
        self.assertIn('full_text 1', html)

        self.assertIn('title 2', html)
        self.assertIn('/blog/slug-2', html)
        self.assertNotIn('summary 2', html)
        self.assertIn('full_text 2', html)

    def test_home_page_displays_articles_in_correct_order(self):
        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full_text 1',
            category='category-1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-1',
            og_image=File(open('test_images/test_image_1.png', 'rb'))
        )
        Article.objects.create(
            title='title 2',
            summary='summary 2',
            full_text='full_text 2',
            category='category-1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-2',
            og_image=File(open('test_images/test_image_1.png', 'rb'))
        )

        url = reverse('home_page')
        response = self.client.get(url)
        html = response.content.decode('utf8')

        self.assertTrue(html.find('title 1') > html.find('title 2'))

    def test_home_page_returns_correct_html(self):
        url = reverse('home_page')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home_page.html')


class ArticleModelTest(TestCase):

    def test_article_model_save_and_retrieve(self):
        # создай статью 1
        # сохрани статью 1 в базе
        article1 = Article(
            title='article 1',
            full_text='full_text 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-1',
            og_image=File(open('test_images/test_image_1.png', 'rb'))
        )
        article1.save()

        # создай статью 2
        # сохрани статью 2 в базе
        article2 = Article(
            title='article 2',
            full_text='full_text 2',
            summary='summary 2',
            category='category 2',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-2',
            og_image=File(open('test_images/test_image_2.png', 'rb'))
        )
        article2.save()

        # загрузи из базы все статьи
        all_articles = Article.objects.all()

        # проверь: статей должно быть 2
        self.assertEqual(len(all_articles), 2)
        # проверь: первая загруженная из базы статья == статья 1
        self.assertEqual(
            all_articles[0].title,
            article1.title
        )
        self.assertEqual(
            all_articles[0].slug,
            article1.slug
        )

        self.assertEqual(
            all_articles[0].og_image,
            article1.og_image
        )

        # проверь: вторая загруженная из базы статья == статья 2
        self.assertEqual(
            all_articles[1].title,
            article2.title
        )
        self.assertEqual(
            all_articles[1].slug,
            article2.slug
        )

        self.assertEqual(
            all_articles[1].og_image,
            article2.og_image
        )
