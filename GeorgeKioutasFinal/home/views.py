from django.shortcuts import render
from shop.models import Product
from trips.views import trips_list

# This view shows the home page template
def home(request):
    # Read the last category that the user opened
    last_category = request.session.get("last_category", "")

    # Start with no recommendations until a category has been visited
    recommended_products = []
    recommendation_category = ""

    # This simple recommendation uses the last shop category the user opened
    if last_category:
        recommendation_category = last_category

        # Find products that belong to that same category
        for product in Product.objects.all():
            if product.category.name == recommendation_category:
                recommended_products.append(product)

            # Only three products are needed for the home carousel
            if len(recommended_products) == 3:
                break

    # The home page needs trips so latest activity can show them
    return render(request, "home/home.html", {
        "trips": trips_list,
        "recommended_products": recommended_products,
        "recommendation_category": recommendation_category,
    })
