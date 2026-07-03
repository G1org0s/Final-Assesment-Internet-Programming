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
from django.urls import include, path
from home import views

# This is the main urls file for the whole Django project.
urlpatterns = [
    # Admin page that Django creates.
    path("admin/", admin.site.urls),

    # Empty path opens the home page first.
    path("", views.home, name="home"),      

    #each app keeps its own page urls here.
    path("", include("home.urls")),
    path("", include("trips.urls")),
    path("", include("analytics.urls")),
    path("", include("reviews.urls")),
    path("", include("about.urls")),
    path("", include("contact.urls")),
    path("", include("shop.urls")),
]
