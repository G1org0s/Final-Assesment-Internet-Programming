from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def index(request):
    return render(request, "tasks.html")