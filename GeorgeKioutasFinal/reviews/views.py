from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ReviewForm
from .models import Review


# This view opens the reviews page and checks the review form.
def reviews(request):
    # Only logged in users can open and write reviews.
    if not request.user.is_authenticated:
        return redirect("/login/")

    # POST is used when the user submits the review form.
    if request.method == "POST":
        form = ReviewForm(request.POST)

        # Django checks if the values follow the form rules.
        if form.is_valid():
            # Create saves the new review in the database.
            Review.objects.create(
                name=request.user.username,
                location=form.cleaned_data["location"],
                fish=form.cleaned_data["fish"],
                message=form.cleaned_data["message"],
                recommend=form.cleaned_data["recommend"],
                stars=0
            )

            # Redirect stops the same form from being submitted again on refresh.
            return redirect("/reviews/")
        else:
            # If validation fails, the page opens again with error messages.
            return render(request, "reviews/reviews.html", {
                "form": form,
                "reviews": Review.objects.all(),
            })
    else:
        # A blank form is made when the page opens normally.
        form = ReviewForm()

    # All gets the saved reviews from the database.
    all_reviews = Review.objects.all()

    # Send the form and saved reviews to the template.
    return render(request, "reviews/reviews.html", {
        "form": form,
        "reviews": all_reviews,
    })


def rate_review(request):
    # Only logged in users can rate a review.
    if not request.user.is_authenticated:
        return HttpResponse("Login required")

    if request.method == "GET":
        # The review id comes from the ajax data.
        review_id = request.GET["review_id"]
        stars = request.GET["stars"]

        # Get finds the review from the database using its id.
        review = Review.objects.get(pk=review_id)

        # Save stores the selected stars in the database.
        review.stars = stars
        review.save()
        return HttpResponse(review.stars)

    return HttpResponse("Invalid request")
