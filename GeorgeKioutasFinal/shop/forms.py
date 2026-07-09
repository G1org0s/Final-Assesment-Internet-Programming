from django import forms
from .models import Product


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
# ModelForm connects this form directly with the Product database model
class ProductEditForm(forms.ModelForm):
    # FileField creates the box that lets the manager choose a photo from their computer
    # required=False means that adding a photo is optional
    photo_file = forms.FileField(label="Product Photo", required=False)

    # Meta tells the form which model and fields it uses
    class Meta:
        model = Product
        fields = ["name", "brand", "price", "category", "sub_category"]
