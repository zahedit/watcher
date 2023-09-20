# Import the django model module
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Game(models.Model):
    title = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    platform = models.CharField(max_length=256)
    release_date = models.DateField()
    age_rating = models.CharField(max_length=128)
    cover = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class UserGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"

#############################################
class Movie(models.Model):
    title = models.CharField(max_length=256) 
    genre = models.CharField(max_length=256) 
    director = models.CharField(max_length=256) 
    release_date = models.DateField() 
    rating = models.CharField(max_length=128) 
    cover = models.URLField(blank=True) 
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class UserMovie(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) 
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)]) 
    review = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"
#############################################
class TVShow(models.Model): 
    title = models.CharField(max_length=256) 
    genre = models.CharField(max_length=256) 
    start_date = models.DateField() 
    end_date = models.DateField(null=True, blank=True) 
    seasons = models.IntegerField() 
    rating = models.CharField(max_length=128) 
    cover = models.URLField(blank=True) 
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title

class UserTVShow(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    tvshow = models.ForeignKey(TVShow, on_delete=models.CASCADE) 
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)]) 
    review = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.tvshow.title}"
