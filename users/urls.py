from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page='home_page'), name='logout'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('profile/', views.profile, name='profile'),
    path('my/', views.my, name='my'),
]