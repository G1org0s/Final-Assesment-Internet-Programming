from django.urls import path
from . import views

# This name lets templates use urls like home:home.
app_name = "home"

# This url sends the home link to the home view.
urlpatterns = [
    path('home/', views.home, name='home'),
]
