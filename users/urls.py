from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='registration'),
    path('login/', views.login, name='login'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('profile/', views.profile, name='profile'),
    path('my/', views.my, name='my'),
]