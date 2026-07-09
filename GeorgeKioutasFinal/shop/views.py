from django.shortcuts import redirect, render
from .forms import ProductEditForm, ProductSearchForm, SubCategoryForm
from .models import Category, Product, SubCategory


def can_manage_products(user):
    # Managers and salesmen can use the custom product management page


    if not user.is_authenticated:
        return False

    # filter searches for the group name and exists returns True when it is found
    is_salesman = user.groups.filter(name="Salesmen").exists()
    is_manager = user.groups.filter(name="Managers").exists()

    # The page opens when at least one group check is true
    return is_salesman or is_manager


def is_manager(user):
    # Managers can see and edit all products
    if not user.is_authenticated:
        return False

    # exists returns True when this user belongs to the Managers group
    return user.groups.filter(name="Managers").exists()


def save_product_photo(product, photo_file):
    # Uploaded product photos are saved in the shop static products folder
    if not photo_file:
        return

    # Use the product id so every product gets its own photo name
    file_name = "product_" + str(product.id) + ".png"

    # This is the folder where the photo will be saved
    file_path = "shop/static/shop/products/" + file_name

    # open creates the new image file at the selected folder path
    # wb means that the file is opened for writing image data
    with open(file_path, "wb") as new_file:
        # read gets the uploaded photo and write saves it in the new file
        new_file.write(photo_file.read())

    # Keep only the photo path inside the database product
    product.photo = "shop/products/" + file_name
    product.save()


# This small function is used when products are sorted by price
def product_price(shop_item):
    # The sorting command uses the returned product price
    return shop_item.price


# This view opens the main shop page with only the category cards


def shop(request):
    # Read every category from the database for the category cards
    return render(request, "shop/shop.html", {
        "categories": Category.objects.all(),
    })


def show_category(request, category_name, template_name):
    # Keep the last category opened for the recommendation
    request.session["last_category"] = category_name

    # At first, every item in the clicked category is shown
    selected_sub_category = "All"
    search_form = ProductSearchForm()
    search_done = False
    search_name = ""
    brand = "All"
    min_price = None
    max_price = None
    price_order = "none"

    if request.method == "POST" and "sub_category" in request.POST:
        # This POST came from the sub category buttons
        form = SubCategoryForm(request.POST)

        # Django checks that the selected sub category is allowed
        if form.is_valid():
            selected_sub_category = form.cleaned_data["sub_category"]
    else:
        # This empty form is used when the category page opens normally
        form = SubCategoryForm()

    if request.method == "POST" and "search_button" in request.POST:
        # This POST came from the product search button
        search_form = ProductSearchForm(request.POST)

        # Django checks the search form before using the values
        if search_form.is_valid():
            search_done = True
            # lower makes the name search work with capital or small letters
            search_name = search_form.cleaned_data["search_name"].lower()
            brand = search_form.cleaned_data["brand"]
            min_price = search_form.cleaned_data["min_price"]
            max_price = search_form.cleaned_data["max_price"]
            price_order = search_form.cleaned_data["price_order"]

    sub_categories = ["All"]

    # These are the sub categories used by products in this category
    for shop_item in Product.objects.all():
        # Only look at products from the category page that is open
        category_matches = shop_item.category.name == category_name

        # Add each used sub category once
        if category_matches and shop_item.sub_category.name not in sub_categories:
            sub_categories.append(shop_item.sub_category.name)

    available_brands = []

    # This finds only the brands that exist in the selected category/type
    for shop_item in Product.objects.all():
        category_matches = shop_item.category.name == category_name

        # All accepts every type, otherwise the names must match
        sub_category_matches = (
            selected_sub_category == "All" or
            shop_item.sub_category.name == selected_sub_category
        )

        # Do not add the same brand more than once
        if category_matches and sub_category_matches and shop_item.brand not in available_brands:
            available_brands.append(shop_item.brand)

    # Reset the brand when it is not used by the selected product type
    if brand not in available_brands:
        brand = "All"

    shown_items = []

    # This loop keeps only items from the chosen category, sub category, and search filters
    for shop_item in Product.objects.all():
        # Each variable checks one search or filter rule
        category_matches = shop_item.category.name == category_name
        sub_category_matches = (
            selected_sub_category == "All" or
            shop_item.sub_category.name == selected_sub_category
        )
        name_matches = search_name == "" or search_name in shop_item.name.lower()
        brand_matches = brand == "All" or shop_item.brand == brand
        min_price_matches = min_price is None or shop_item.price >= min_price
        max_price_matches = max_price is None or shop_item.price <= max_price

        # The product is shown only when every check is true
        if category_matches and sub_category_matches and name_matches and brand_matches and min_price_matches and max_price_matches:
            shown_items.append(shop_item)

    # This sorts the products by price only when the user asks for it
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


# These views open each shop category page


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


def manage_products(request):
    # Customers and public users are not allowed to open this page
    if not can_manage_products(request.user):
        return redirect("/home/")

    if is_manager(request.user):
        # Managers can see every product in the database
        products = Product.objects.all()
    else:
        # Salesmen see only products that belong to them
        products = Product.objects.filter(owner=request.user)

    return render(request, "shop/manage_products.html", {
        "products": products,
        "is_manager": is_manager(request.user),
    })


def add_product(request):
    # Only managers can add new products
    if not is_manager(request.user):
        return redirect("/shop/manage/")

    if request.method == "POST":
        # Put the submitted values inside the product form
        form = ProductEditForm(request.POST)

        if form.is_valid():
            # Wait before saving because the owner must be added first
            product = form.save(commit=False)

            # The logged in manager becomes the product owner
            product.owner = request.user

            # This command adds the complete product to the database
            product.save()

            # Save the optional uploaded image after the product has an id
            save_product_photo(product, request.FILES.get("photo_file"))
            return redirect("/shop/manage/")
    else:
        # Show an empty product form when the page first opens
        form = ProductEditForm()

    return render(request, "shop/add_product.html", {
        "form": form,
    })


def edit_product(request, product_id):
    # Customers and public users are not allowed to edit products
    if not can_manage_products(request.user):
        return redirect("/home/")

    # Find the selected product from its number in the url
    product = Product.objects.get(id=product_id)

    # Salesmen cannot open products that do not belong to them
    if not is_manager(request.user) and product.owner != request.user:
        return redirect("/shop/manage/")

    if request.method == "POST":
        # instance means this form updates the existing product
        form = ProductEditForm(request.POST, instance=product)

        if form.is_valid():
            # Save the edited product values in the database
            product = form.save()
            save_product_photo(product, request.FILES.get("photo_file"))
            return redirect("/shop/manage/")
    else:
        # Fill the form with the product's current values
        form = ProductEditForm(instance=product)

    return render(request, "shop/edit_product.html", {
        "form": form,
        "product": product,
    })


def delete_product(request, product_id):
    # Only managers can delete products from the custom page
    if not is_manager(request.user):
        return redirect("/shop/manage/")

    if request.method == "POST":
        # Find the selected database product and remove it
        product = Product.objects.get(id=product_id)
        product.delete()

    return redirect("/shop/manage/")
