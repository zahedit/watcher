from django.urls import path
from .views import search_form, search_games, add_game, search_movies, search_tv, add_tv
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('search/', views.search_form, name='search'),
    path('search/game/', views.search_games, name='result_game'),
    path('search/movie/', views.search_movies, name='result_movie'),
    path('search/tv/', views.search_tv, name='result_tv'),
    path('add/game/', views.add_game, name='add_game'),
    path('add/movie/', views.add_movie, name='add_movie'),
    path('add/tv/', views.add_tv, name='add_tv'),
]
