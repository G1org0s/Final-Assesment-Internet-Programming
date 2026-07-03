from django.urls import path
from . import views

# This name lets Django know these urls belong to analytics.
app_name = "analytics"

# This url sends the analytics link to the analytics view.
urlpatterns = [
    path('analytics/', views.analytics, name='analytics'),
]
