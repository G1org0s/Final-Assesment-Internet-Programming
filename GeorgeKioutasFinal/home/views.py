from django.shortcuts import render
from trips.views import trips_list

# This view shows the home page template.
def home(request):
    # The home page needs trips so latest activity can show them.
    return render(request, "home/home.html", {
        "trips": trips_list,
    })
