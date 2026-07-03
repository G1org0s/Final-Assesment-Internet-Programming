from django.urls import path
from . import views

# This name lets Django know these urls belong to about.
app_name = "about"

# This url sends the about link to the about view.
urlpatterns = [
    path('about/', views.about, name='about'),
]
