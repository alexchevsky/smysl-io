from django.shortcuts import render
from .models import Article


def home_page(request):
    articles = Article.objects.order_by('-pubdate')
    context = {'articles': articles}
    return render(request, 'home_page.html', context)


def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'article_page.html', context)


def category_page(request, category):
    articles = Article.objects.filter(category=category)
    context = {'articles': articles, 'category': category}
    return render(request, 'category_page.html', context)
