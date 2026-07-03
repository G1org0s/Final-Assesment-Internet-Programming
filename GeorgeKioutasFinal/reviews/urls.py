from django.urls import path
from . import views

# This name lets the form use reviews:reviews in the template.
app_name = "reviews"

# This url sends the reviews link to the reviews view.
urlpatterns = [
    path('reviews/', views.reviews, name='reviews'),
]
