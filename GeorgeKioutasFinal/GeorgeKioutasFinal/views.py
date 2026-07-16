# from django.http import HttpResponse
from django.shortcuts import render



# This section opens the simple home page used by the main project url


def homepage(request):
  #  return HttpResponse("Hello World! This is the Home Page.")
  return render(request, 'home.html')



