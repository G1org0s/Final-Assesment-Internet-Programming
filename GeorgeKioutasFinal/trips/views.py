from django.shortcuts import render

# This view opens the trips planner page.
def trips(request):
    return render(request, "trips/trips.html")
