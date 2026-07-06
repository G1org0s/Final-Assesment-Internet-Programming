from django import forms
from django.shortcuts import render
from .models import Category, Product, SubCategory


# This form is used for filtering inside a category page.
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


class ProductSearchForm(forms.Form):
    # This form searches products by name, brand, price, and price order.
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


# This small function is used when products are sorted by price.
def product_price(shop_item):
    return shop_item.price


# This view opens the main shop page with only the category cards.
def shop(request):
    return render(request, "shop/shop.html", {
        "categories": Category.objects.all(),
    })


def show_category(request, category_name, template_name):
    # When a logged-in user opens a category, keep it for the dashboard.
    if request.user.is_authenticated:
        recent_categories = request.session.get("recent_categories", [])

        if category_name in recent_categories:
            recent_categories.remove(category_name)

        recent_categories.insert(0, category_name)
        request.session["recent_categories"] = recent_categories[:5]

    # At first, every item in the clicked category is shown.
    selected_sub_category = "All"
    search_form = ProductSearchForm()
    search_done = False
    search_name = ""
    brand = "All"
    min_price = None
    max_price = None
    price_order = "none"

    if request.method == "POST" and "sub_category" in request.POST:
        form = SubCategoryForm(request.POST)

        # Django checks that the selected sub category is allowed.
        if form.is_valid():
            selected_sub_category = form.cleaned_data["sub_category"]
    else:
        # This empty form is used when the category page opens normally.
        form = SubCategoryForm()

    if request.method == "POST" and "search_button" in request.POST:
        search_form = ProductSearchForm(request.POST)

        # Django checks the search form before using the values.
        if search_form.is_valid():
            search_done = True
            search_name = search_form.cleaned_data["search_name"].lower()
            brand = search_form.cleaned_data["brand"]
            min_price = search_form.cleaned_data["min_price"]
            max_price = search_form.cleaned_data["max_price"]
            price_order = search_form.cleaned_data["price_order"]

    sub_categories = ["All"]

    # These are the sub categories that belong to the current page category.
    for sub_category in SubCategory.objects.all():
        if sub_category.category.name == category_name:
            sub_categories.append(sub_category.name)

    available_brands = []

    # This finds only the brands that exist in the selected category/type.
    for shop_item in Product.objects.all():
        category_matches = shop_item.sub_category.category.name == category_name
        sub_category_matches = (
            selected_sub_category == "All" or
            shop_item.sub_category.name == selected_sub_category
        )

        if category_matches and sub_category_matches and shop_item.brand not in available_brands:
            available_brands.append(shop_item.brand)

    if brand not in available_brands:
        brand = "All"

    shown_items = []

    # This loop keeps only items from the chosen category, sub category, and search filters.
    for shop_item in Product.objects.all():
        category_matches = shop_item.sub_category.category.name == category_name
        sub_category_matches = (
            selected_sub_category == "All" or
            shop_item.sub_category.name == selected_sub_category
        )
        name_matches = search_name == "" or search_name in shop_item.name.lower()
        brand_matches = brand == "All" or shop_item.brand == brand
        min_price_matches = min_price is None or shop_item.price >= min_price
        max_price_matches = max_price is None or shop_item.price <= max_price

        if category_matches and sub_category_matches and name_matches and brand_matches and min_price_matches and max_price_matches:
            shown_items.append(shop_item)

    # This sorts the products by price only when the user asks for it.
    if price_order == "low":
        shown_items.sort(key=product_price)
    elif price_order == "high":
        shown_items.sort(key=product_price, reverse=True)

    return render(request, template_name, {
        "form": form,
        "search_form": search_form,
        "search_done": search_done,
        "available_brands": available_brands,
        "selected_brand": brand,
        "category_name": category_name,
        "selected_sub_category": selected_sub_category,
        "sub_categories": sub_categories,
        "items": shown_items,
    })


# These views open each shop category page.
def rods(request):
    return show_category(request, "Rods", "shop/rods.html")


def reels(request):
    return show_category(request, "Reels", "shop/reels.html")


def lines(request):
    return show_category(request, "Lines", "shop/lines.html")


def lures(request):
    return show_category(request, "Lures", "shop/lures.html")


def accessories(request):
    return show_category(request, "Accessories", "shop/accessories.html")
