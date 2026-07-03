from django.urls import path
from . import views

# This name lets the form use trips:trips in the template.
app_name = "trips"

# This url sends the trips link to the trips view.
urlpatterns = [
    path('trips/', views.trips, name='trips'),
]
