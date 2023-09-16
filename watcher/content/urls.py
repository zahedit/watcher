from django.urls import path
from .views import search_form, search_games
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('search/', views.search_form, name='search'),
    path('result/', views.search_games, name='result'),
]
