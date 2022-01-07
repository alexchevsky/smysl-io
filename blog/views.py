from django.shortcuts import render
from .models import Article
# from django.http import HttpResponse

def home_page(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'home_page.html', context)


def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'article_page.html', context)
