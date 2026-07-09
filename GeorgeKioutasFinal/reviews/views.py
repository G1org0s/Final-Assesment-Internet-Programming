from django.shortcuts import render
from .forms import ReviewForm


# Reviews are saved in this list while the server is running.
reviews_list = []


# This view opens the reviews page and checks the review form.
def reviews(request):
    # POST is used when the user submits the review form.
    if request.method == "POST":
        form = ReviewForm(request.POST)

        # Django checks if the values follow the form rules.
        if form.is_valid():
            # The review has many values, so they are kept together in one dictionary.
            reviews_list.append({
                "name": form.cleaned_data["name"],
                "location": form.cleaned_data["location"],
                "fish": form.cleaned_data["fish"],
                "message": form.cleaned_data["message"],
                "recommend": form.cleaned_data["recommend"],
            })
        else:
            # If validation fails, the page opens again with error messages.
            return render(request, "reviews/reviews.html", {
                "form": form,
                "reviews": reviews_list,
            })
    else:
        # A blank form is made when the page opens normally.
        form = ReviewForm()

    # Send the form and saved reviews to the template.
    return render(request, "reviews/reviews.html", {
        "form": form,
        "reviews": reviews_list,
    })
