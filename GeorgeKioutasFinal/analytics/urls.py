from django.urls import path
from . import views

# This url sends the analytics link to the analytics view.
urlpatterns = [
    path('analytics/', views.analytics, name='analytics'),
]
