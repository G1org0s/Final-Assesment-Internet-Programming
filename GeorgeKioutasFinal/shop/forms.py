from django import forms
from .models import Category, SubCategory


# This form is used for filtering inside a category page
class SubCategoryForm(forms.Form):
    sub_category = forms.ChoiceField(
        label="Sub Category",
        choices=[
            ("All", "All"),
            ("Spinning", "Spinning"),
            ("Casting", "Casting"),
            ("Surfcasting", "Surfcasting"),
            ("Jigging", "Jigging"),
            ("Boat Fishing", "Boat Fishing"),
            ("General", "General"),
        ]
    )


# This form searches products by name, brand, price, and price order
class ProductSearchForm(forms.Form):
    search_name = forms.CharField(label="Item Name", required=False)
    brand = forms.CharField(label="Brand", required=False)
    min_price = forms.IntegerField(label="Minimum Price", required=False, min_value=0)
    max_price = forms.IntegerField(label="Maximum Price", required=False, min_value=0)
    price_order = forms.ChoiceField(
        label="Sort Price",
        required=False,
        choices=[
            ("none", "No sorting"),
            ("low", "Lowest first"),
            ("high", "Highest first"),
        ]
    )


# This form is for the custom manager and salesman product pages
class ProductEditForm(forms.Form):
    # These fields are written by the manager or salesman
    name = forms.CharField(max_length=200)
    brand = forms.CharField(max_length=100)
    price = forms.IntegerField(min_value=0)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.all())

    # FileField creates the box that lets the manager choose a photo from their computer
    # required=False means that adding a photo is optional
    photo_file = forms.FileField(label="Product Photo", required=False)


# This form lets a manager add a new main category
class CategoryAddForm(forms.Form):
    name = forms.CharField(max_length=100)

    # FileField creates the box that lets the manager choose a category photo
    photo_file = forms.FileField(label="Category Photo")


# This form lets a manager add a new sub category
class SubCategoryAddForm(forms.Form):
    # Sub categories are reused by products, like Spinning or Casting
    name = forms.CharField(max_length=100)

    # The manager chooses which main category this sub category belongs to
    category = forms.ModelChoiceField(queryset=Category.objects.all())
