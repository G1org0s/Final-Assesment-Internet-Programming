from django.shortcuts import render

# This view opens the about page.
def about(request):
    return render(request, "about/about.html")
