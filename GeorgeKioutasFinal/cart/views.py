from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CheckoutForm
from .models import CartItem
from shop.models import Product


# This small function calculates the cart prices
def cart_prices(cart_items):
    # Start from zero before adding the product prices
    total_price = 0

    # Add each product price times its quantity
    for cart_item in cart_items:
        total_price = total_price + cart_item.product.price * cart_item.quantity

    # The product price is shown as the final price with tax
    tax = total_price * 24 / 100

    # This shows the price after removing the 24 percent tax
    price_without_tax = total_price - tax

    return price_without_tax, tax, total_price


def cart(request):
    # Only logged in users can use the cart
    if not request.user.is_authenticated:
        return redirect("/login/")

    # Get only the cart items of the logged in user
    cart_items = CartItem.objects.filter(user=request.user)

    # Use the helper function above so the same price code is not repeated
    price_without_tax, tax, total_price = cart_prices(cart_items)

    # Send the cart items and prices to the html page
    return render(request, "cart/cart.html", {
        "cart_items": cart_items,
        "price_without_tax": price_without_tax,
        "tax": tax,
        "total_price": total_price,
    })


def add_to_cart(request):
    # Only logged in users can add products to the cart
    if not request.user.is_authenticated:
        return redirect("/login/")

    if request.method == "POST":
        # The product id comes from the hidden form input
        product_id = request.POST["product_id"]

        # This keeps the user on the same shop page after adding to cart
        next_page = request.POST["next"]

        # Find the product from the database using the id from the form
        product = Product.objects.get(id=product_id)

        # Check if this product is already in this user's cart
        existing_items = CartItem.objects.filter(user=request.user, product=product)

        if existing_items:
            # If it already exists, increase the quantity
            cart_item = existing_items[0]
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
        else:
            # If it does not exist, create a new cart item
            CartItem.objects.create(
                user=request.user,
                product=product,
                quantity=1
            )

        # Show a small message and keep the user on the same shop page
        messages.success(request, "Product added to cart.")
        return redirect(next_page)

    return redirect("/shop/")


def increase_quantity(request):
    # Only logged in users can change their cart
    if not request.user.is_authenticated:
        return redirect("/login/")

    if request.method == "POST":
        # Find the selected cart item and add one
        cart_item_id = request.POST["cart_item_id"]

        # user=request.user makes sure the user changes only his own cart item
        cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)
        cart_item.quantity = cart_item.quantity + 1
        cart_item.save()

    return redirect("/cart/")


def decrease_quantity(request):
    # Only logged in users can change their cart
    if not request.user.is_authenticated:
        return redirect("/login/")

    if request.method == "POST":
        # Find the selected cart item and remove one
        cart_item_id = request.POST["cart_item_id"]

        # user=request.user protects another user's cart item from being changed
        cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)
        cart_item.quantity = cart_item.quantity - 1

        # Delete the item if quantity becomes zero
        if cart_item.quantity <= 0:
            cart_item.delete()
        else:
            cart_item.save()

    return redirect("/cart/")


def delete_item(request):
    # Only logged in users can delete from their cart
    if not request.user.is_authenticated:
        return redirect("/login/")

    if request.method == "POST":
        # Find the selected cart item and delete it
        cart_item_id = request.POST["cart_item_id"]

        # Find the cart item that belongs to the logged in user
        cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)
        cart_item.delete()

    return redirect("/cart/")


def checkout(request):
    # Only logged in users can open checkout
    if not request.user.is_authenticated:
        return redirect("/login/")

    # Load the products that are currently inside the user's cart
    cart_items = CartItem.objects.filter(user=request.user)

    # Calculate the total price again for the checkout summary
    price_without_tax, tax, total_price = cart_prices(cart_items)

    if request.method == "POST":
        # Puts the submitted checkout details inside the form
        form = CheckoutForm(request.POST)

        if form.is_valid():


            
            # This simulates a purchase by emptying the cart after checkout
            cart_items.delete()
            return redirect("/cart/")
    else:
        # Show an empty checkout form when the page first opens
        form = CheckoutForm()

    # Send the form, cart products and prices to the checkout html page
    return render(request, "cart/checkout.html", {
        "form": form,
        "cart_items": cart_items,
        "price_without_tax": price_without_tax,
        "tax": tax,
        "total_price": total_price,
    })
