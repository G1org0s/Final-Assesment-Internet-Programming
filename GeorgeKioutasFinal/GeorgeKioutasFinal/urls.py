"""
URL configuration for GeorgeKioutasFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from trips import views as trips_views
from analytics import views as analytics_views
from reviews import views as reviews_views
from about import views as about_views
from contact import views as contact_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Empty path opens the home page first.
    path("", views.home, name="home"),       # opens at http://127.0.0.1:8000/
    path("home/", views.home, name="home"),  # opens at http://127.0.0.1:8000/home/

    # Each path connect a page name with the correct view function.
    path("trips/", trips_views.trips, name="trips"),
    path("analytics/", analytics_views.analytics, name="analytics"),
    path("reviews/", reviews_views.reviews, name="reviews"),
    path("about/", about_views.about, name="about"),
    path("contact/", contact_views.contact, name="contact"),
]
