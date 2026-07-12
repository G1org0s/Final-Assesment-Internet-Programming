from django.urls import path
from . import views

# This name lets templates call cart urls by nickname
app_name = "cart"

urlpatterns = [
    # This opens the main cart page
    path("cart/", views.cart, name="cart"),

    # This url is used when the user presses add to cart
    path("cart/add/", views.add_to_cart, name="add_to_cart"),

    # These two urls change the product quantity
    path("cart/increase/", views.increase_quantity, name="increase_quantity"),
    path("cart/decrease/", views.decrease_quantity, name="decrease_quantity"),

    # This url deletes a product from the cart
    path("cart/delete/", views.delete_item, name="delete_item"),

    # This opens the checkout page
    path("cart/checkout/", views.checkout, name="checkout"),
]
