from django.urls import path
from . import views

# This url sends the contact link to the contact view.
urlpatterns = [
    path('contact/', views.contact, name='contact'),
]
