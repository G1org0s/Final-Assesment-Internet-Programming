from django.urls import path
from . import views

# This url sends the about link to the about view.
urlpatterns = [
    path('about/', views.about, name='about'),
]
