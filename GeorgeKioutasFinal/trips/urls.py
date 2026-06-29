from django.urls import path
from . import views

# This url sends the trips link to the trips view.
urlpatterns = [
    path('trips/', views.trips, name='trips'),
]
