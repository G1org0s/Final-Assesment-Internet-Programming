from django.db import models


# This table keeps the main product categories, like Rods and Reels.
class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=200)

    # This makes the admin page show the category name.
    def __str__(self):
        return self.name


# This table keeps the smaller categories that belong to one main category.
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # This makes the admin page show the sub category name.
    def __str__(self):
        return self.name


# This table keeps the products that users can search and filter.
class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    # This makes the admin page show the product name.
    def __str__(self):
        return self.name
