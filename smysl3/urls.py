"""smysl3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import home_page, article_page, category_page
from courses.views import python_redirect, setup_redirect, dev_redirect, \
                          trello_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('blog/<slug:slug>/', article_page, name='article_page'),
    path('blog/category/<slug:category>/', category_page,
         name='category_page'),
    path('python/', python_redirect, name='python_redirect'),
    path('setup/', setup_redirect, name='setup_redirect'),
    path('dev/', dev_redirect, name='dev_redirect'),
    path('trello/', trello_redirect, name='trello_redirect'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
