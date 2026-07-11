from django.contrib import admin
from .models import Review


# This lets the admin see and manage reviews.
admin.site.register(Review)
