from django import forms
from .models import Category, SubCategory


# These are the forms customers use to filter and search shop items





class SubCategoryForm(forms.Form):
    # CharField lets the page use new sub categories added by the manager
    sub_category = forms.CharField(label="Sub Category", max_length=100)


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









# These are the forms used by managers and salesmen to manage shop data






class ProductEditForm(forms.Form):
    # These text fields can have up to 60 characters
    name = forms.CharField(max_length=60)
    brand = forms.CharField(max_length=60)

    # Price is a number and can have up to five digits
    price = forms.IntegerField(min_value=0, max_value=99999)

    # A description is optional and can have up to 60 characters
    description = forms.CharField(required=False, max_length=60)

    # These fields let the manager choose saved categories from the database
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.all())

    # FileField creates the box that lets the manager choose a photo from their computer
    # required=False means that adding a photo is optional
    photo_file = forms.FileField(label="Product Photo", required=False)






# This form lets a manager add a new main category



class CategoryAddForm(forms.Form):
    # The category name can have up to 60 characters
    name = forms.CharField(max_length=60)

    # FileField creates the box that lets the manager choose a category photo
    photo_file = forms.FileField(label="Category Photo")








# This form lets a manager add a new sub category



class SubCategoryAddForm(forms.Form):
    # The sub category name can have up to 60 characters
    name = forms.CharField(max_length=60)

    # The manager chooses which main category this sub category belongs to
    category = forms.ModelChoiceField(queryset=Category.objects.all())
