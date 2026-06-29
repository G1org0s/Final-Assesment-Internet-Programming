# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
  #  return HttpResponse("Hello World! This is the Home Page.")
  return render(request, 'home.html')



