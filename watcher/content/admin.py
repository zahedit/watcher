from django.contrib import admin
from .models import Game, UserGame, Movie, UserMovie, TVShow, UserTVShow

# Register your models here.
admin.site.register(Game)
admin.site.register(UserGame)
admin.site.register(Movie)
admin.site.register(UserMovie)
admin.site.register(TVShow)
admin.site.register(UserTVShow)