from django import forms
from django.shortcuts import render


# This form is for writing a fishing review.
class ReviewForm(forms.Form):
    # min_length and max_length are used for simple validation.
    name = forms.CharField(label="Name", min_length=2, max_length=30)
    location = forms.CharField(label="Location", min_length=2, max_length=30)
    fish = forms.CharField(label="Fish Caught", max_length=80)
    # Textarea makes the message box bigger than a normal input.
    message = forms.CharField(
        label="Message",
        min_length=10,
        max_length=200,
        widget=forms.Textarea
    )
    # The user can only answer Yes or No here.
    recommend = forms.ChoiceField(
        label="Would you recommend this location?",
        choices=[
            ("Yes", "Yes"),
            ("No", "No"),
        ]
    )


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
