from django.urls import path
from . import views

# This name lets the form use contact:contact in the template.
app_name = "contact"

# This url sends the contact link to the contact view.
urlpatterns = [
    path('contact/', views.contact, name='contact'),
]
