from django.urls import path
from . import views

# This url sends the reviews link to the reviews view.
urlpatterns = [
    path('reviews/', views.reviews, name='reviews'),
]
