from django.urls import path
from . import views

# This url sends the home link to the home view.
urlpatterns = [
    path('home/', views.home, name='home'),
]
