from django.db import models
from django.contrib.auth.models import User


# This table keeps the main product categories, like Rods and Reels
class Category(models.Model):
    # Each category has a name and the path of its card photo
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=200)

    # __str__ returns the readable category name shown in Django Admin
    def __str__(self):
        return self.name


# This table keeps the subcategories that belong to one main category
class SubCategory(models.Model):
    # A sub category has a name, like Spinning or Casting
    name = models.CharField(max_length=100)

    # This connects the sub category with one main category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    # __str__ returns the readable sub category name shown in Django Admin
    def __str__(self):
        return self.name


# This table keeps the products that users can search and filter
class Product(models.Model):
    # These fields keep the main information for each product
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()

    # The database keeps the photo path, not the actual image file
    photo = models.CharField(max_length=200, blank=True)

    # This foreign key connects the product with one main category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # This foreign key connects the product with one sub category
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    # Owner decides which salesman is allowed to edit the product
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # __str__ returns the readable product name shown in Django Admin
    def __str__(self):
        return self.name
