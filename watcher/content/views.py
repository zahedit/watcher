import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Game

# @csrf_exempt
# def search(request):
#     if request.method == "POST":
#         game_name = request.POST.get("game_name")
#         url = f"{BASE_URL}/games?key={API_KEY}&search={game_name}"
#         response = requests.get(url).json()

#         if response["results"]:
#             game = response["results"][0]
#             name = game["name"]
#             slug = game["slug"]
#             released = game["released"]
#             rating = game["rating"]
#             platforms = [p["platform"]["name"] for p in game["platforms"]]
#             genres = [g["name"] for g in game["genres"]]
#             description = game["description"]

#             context = {
#                 "name": name,
#                 "slug": slug,
#                 "released": released,
#                 "rating": rating,
#                 "platforms": platforms,
#                 "genres": genres,
#                 "description": description,
#             }
#             return render(request, "content/search_results.html", context)

#         else:
#             return HttpResponse("No games found with that name.")

#     else:
#         return redirect("home")

api_key = "ea0afd24e6f34b8f84a0802b8585d42d"
base_url = "https://api.rawg.io/api/games"

def search_games(request):
    query = request.GET.get("q", "")

    if not query:
        return HttpResponse("")

    url = f"{base_url}?search={query}&key={api_key}&page_size=1"
    response = requests.get(url)
    data = response.json()
    results = data.get("results", [])


    for result in results:
        game = Game.objects.filter(title=result["name"]).first()
        if not game:
            game = Game(
                title=result["name"],
                genre=", ".join([g["name"] for g in result["genres"]]),
                platform=", ".join([p["platform"]["name"] for p in result["platforms"]]),
                release_date=result["released"],
                age_rating=result["esrb_rating"]["name"] if result["esrb_rating"] else "Unknown",
                cover=result["background_image"],
            )
            game.save()
    return render(request, "content/search_results.html", {"results": results})




def search_form(request):
    return render(request, "content/search_form.html")
