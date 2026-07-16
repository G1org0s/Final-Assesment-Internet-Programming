from django.shortcuts import render

# This section opens the about page
def about(request):
    return render(request, "about/about.html")
