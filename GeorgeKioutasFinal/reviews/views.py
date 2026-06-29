from django.shortcuts import render

# This view opens the reviews page.
def reviews(request):
    return render(request, "reviews/reviews.html")
