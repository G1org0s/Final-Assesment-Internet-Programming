from django.contrib import admin
from .models import CartItem


# This lets the admin see cart items in Django admin
admin.site.register(CartItem)
