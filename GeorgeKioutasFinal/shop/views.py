from django import forms
from django.shortcuts import render


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


# These are the main shop categories and their photos.
categories = [
    {"name": "Rods", "photo": "shop/rod.jpeg", "url": "/shop/Rods"},
    {"name": "Reels", "photo": "shop/reel.jpeg", "url": "/shop/Reels"},
    {"name": "Lines", "photo": "shop/line.jpeg", "url": "/shop/Lines"},
    {"name": "Lures", "photo": "shop/lure.jpeg", "url": "/shop/Lures"},
    {"name": "Accessories", "photo": "shop/accessories.jpeg", "url": "/shop/Accessories"},
]


# These are the sub categories that belong to each main category.
sub_categories = {
    "Rods": ["All", "Spinning", "Casting", "Surfcasting"],
    "Reels": ["All", "Spinning", "Casting", "Boat Fishing"],
    "Lines": ["All", "Spinning", "Casting", "Surfcasting"],
    "Lures": ["All", "Spinning", "Jigging", "Boat Fishing"],
    "Accessories": ["All", "General"],
}


# These are the starting shop items for the page.
shop_items = [
    {"item": "Casting Rod", "category": "Rods", "sub_category": "Casting"},
    {"item": "Spinning Rod", "category": "Rods", "sub_category": "Spinning"},
    {"item": "Surfcasting Rod", "category": "Rods", "sub_category": "Surfcasting"},
    {"item": "Spinning Reel", "category": "Reels", "sub_category": "Spinning"},
    {"item": "Casting Reel", "category": "Reels", "sub_category": "Casting"},
    {"item": "Boat Reel", "category": "Reels", "sub_category": "Boat Fishing"},
    {"item": "Fluorocarbon Line", "category": "Lines", "sub_category": "Spinning"},
    {"item": "Casting Line", "category": "Lines", "sub_category": "Casting"},
    {"item": "Surfcasting Line", "category": "Lines", "sub_category": "Surfcasting"},
    {"item": "Soft Lure", "category": "Lures", "sub_category": "Spinning"},
    {"item": "Jigging Lure", "category": "Lures", "sub_category": "Jigging"},
    {"item": "Boat Lure", "category": "Lures", "sub_category": "Boat Fishing"},
    {"item": "Hook Box", "category": "Accessories", "sub_category": "General"},
    {"item": "Fishing Pliers", "category": "Accessories", "sub_category": "General"},
]


# This view opens the main shop page with only the category cards.
def shop(request):
    return render(request, "shop/shop.html", {
        "categories": categories,
    })


def show_category(request, category_name, template_name):
    # At first, every item in the clicked category is shown.
    selected_sub_category = "All"

    if request.method == "POST":
        form = SubCategoryForm(request.POST)

        # Django checks that the selected sub category is allowed.
        if form.is_valid():
            selected_sub_category = form.cleaned_data["sub_category"]
    else:
        # This empty form is used when the category page opens normally.
        form = SubCategoryForm()

    shown_items = []

    # This loop keeps only items from the chosen category and sub category.
    for shop_item in shop_items:
        category_matches = shop_item["category"] == category_name
        sub_category_matches = (
            selected_sub_category == "All" or
            shop_item["sub_category"] == selected_sub_category
        )

        if category_matches and sub_category_matches:
            shown_items.append(shop_item)

    return render(request, template_name, {
        "form": form,
        "category_name": category_name,
        "selected_sub_category": selected_sub_category,
        "sub_categories": sub_categories[category_name],
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
