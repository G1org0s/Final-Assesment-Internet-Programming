from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


# This table keeps the products that a user has placed in the cart
class CartItem(models.Model):
    # The cart item belongs to one logged in user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # The cart item is connected with one shop product
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Quantity shows how many times this product is in the cart
    quantity = models.IntegerField(default=1)

    # This makes the admin page show the product name for the cart item
    def __str__(self):
        # Return the product name instead of showing CartItem object
        return self.product.name
