import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Game, Movie, TVShow, UserTVShow, UserMovie

from django.contrib.auth.decorators import login_required


api_key_movie = "db9e6b5bb2e44f19d109c9ae67a1bce7"
base_url_movie = "https://api.themoviedb.org/3"

def search_movies(request):
    query = request.GET.get("name", "")

    if not query:
        return HttpResponse("")
    params = {
        "api_key": api_key_movie,
        "query": query,
        "page": 1,
        "page_size": 1,
    }
    response = requests.get(base_url_movie + "/search/movie", params=params)

    if response.status_code == 200:
        data = response.json()
        results = data["results"]
        return render(request, "content/search_results_movie.html", {"results": results})
    else:
        return HttpResponse("Error: " + str(response.status_code))
#############################################
@login_required
def add_movie(request): # get the movie details from the api using the movie id 
    movie_id = request.GET.get('id') 
    url = f"{base_url_movie}/movie/{movie_id}?api_key={api_key_movie}"
    url_credits = f"{base_url_movie}/movie/{movie_id}/credits?api_key={api_key_movie}"
    response = requests.get(url) 
    result = response.json()
    
    response_credits = requests.get(url_credits) 
    result_credits = response_credits.json()
    # check if the movie already exists in the database
    movie = Movie.objects.filter(title=result["title"]).first()
    if not movie:
        # create a new movie object and save it to the database
        movie = Movie(
            title=result["title"],
            genre=", ".join([g["name"] for g in result["genres"]]),
            director=", ".join([d["name"] for d in result_credits["crew"] if d["job"] == "Director"]),
            release_date=result["release_date"],
            rating=result["vote_average"],
            cover=result["poster_path"],
            description=result["overview"],
        )
        movie.save()

    movie_user_searched = Movie.objects.get(title=result["title"])
    qs = UserMovie.objects.filter(user=request.user, movie= movie_user_searched)
    if qs.exists():
        qs.delete()
    else:
        UserMovie.objects.create(user=request.user, movie= movie_user_searched)
    return render(request, "content/confirmation.html", {"movie": movie})
#############################################
def search_tv(request):
    query = request.GET.get("name", "")

    if not query:
        return HttpResponse("")
    params = {
        "api_key": api_key_movie,
        "query": query,
        "page": 1,
        "page_size": 1,
    }
    response = requests.get(base_url_movie + "/search/tv", params=params)

    if response.status_code == 200:
        data = response.json()
        results = data["results"]
        return render(request, "content/search_results_tv.html", {"results": results})
    else:
        return HttpResponse("Error: " + str(response.status_code))
#############################################
@login_required
def add_tv(request): # get the movie details from the api using the movie id 
    tv_id = request.GET.get('id') 
    url = f"{base_url_movie}/tv/{tv_id}?api_key={api_key_movie}"
    response = requests.get(url) 
    result = response.json()
    
    # check if the movie already exists in the database
    tvShow = TVShow.objects.filter(title=result["name"]).first()
    if not tvShow:
        # create a new movie object and save it to the database
        tvShow = TVShow(
            title = result["name"],
            genre=", ".join([g["name"] for g in result["genres"]]),
            start_date = result["first_air_date"],
            end_date = result["last_air_date"],
            seasons = result["number_of_seasons"],
            rating = result["vote_average"],
            cover = result["poster_path"],
            description = result["overview"],
        )
        tvShow.save()
    tvshow_user_searched = TVShow.objects.get(title=result["name"])
    
    qs = UserTVShow.objects.filter(user=request.user, tvshow= tvshow_user_searched)
    if qs.exists():
        qs.delete()
    else:
        UserTVShow.objects.create(user=request.user, tvshow= tvshow_user_searched)
    return render(request, "content/confirmation.html", {"tv": tvShow})
#############################################
api_key_game = "ea0afd24e6f34b8f84a0802b8585d42d"
base_url_game = "https://api.rawg.io/api/games"

def search_games(request):
    query = request.GET.get("q", "")

    if not query:
        return HttpResponse("")

    url = f"{base_url_game}?search={query}&key={api_key_game}&page_size=3"
    response = requests.get(url)
    data = response.json()
    results = data.get("results", [])
    return render(request, "content/search_results.html", {"results": results})
#############################################
@login_required
def add_game(request): # get the game details from the api using the game id 
    game_id = request.GET.get('game_id')
    url = f"{base_url_game}/{game_id}?key={api_key_game}" 
    response = requests.get(url) 
    result = response.json()

    # check if the game already exists in the database
    game = Game.objects.filter(title=result["name"]).first()
    if not game:
        # create a new game object and save it to the database
        game = Game(
            title=result["name"],
            genre=", ".join([g["name"] for g in result["genres"]]),
            platform=", ".join([p["platform"]["name"] for p in result["platforms"]]),
            release_date=result["released"],
            age_rating=result["esrb_rating"]["name"] if result["esrb_rating"] else "Unknown",
            cover=result["background_image"],
        )
        game.save()
    return render(request, "content/confirmation.html", {"game": game})
#############################################
def search_form(request):
    tvshows = TVShow.objects.order_by("-start_date")[:10]
    movies = Movie.objects.order_by("-release_date")[:10]
    games = Game.objects.order_by("-release_date")[:10]
    return render(request, "content/search_form.html", {"tvshows": tvshows,"movies": movies,"games": games})
