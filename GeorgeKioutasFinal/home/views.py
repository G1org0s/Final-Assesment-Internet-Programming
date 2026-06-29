from django.shortcuts import render

# This view shows the home page template.
def home(request):
    return render(request, "home/home.html")
