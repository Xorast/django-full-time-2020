from django.urls import path
from .views import get_first_page, get_2020_page, read_movies, create_movie, update_movie

urlpatterns = [
    path('hello', get_first_page),
    path('year-2020', get_2020_page),
    path('read-movies', read_movies),
    path('create-movie', create_movie),
    path('update-movie/<pk>', update_movie)
]
