from django import forms


# This section has the form used by customers to write a review



class ReviewForm(forms.Form):
    # min_length and max_length are used for simple validation
    location = forms.CharField(label="Location", min_length=2, max_length=30)
    fish = forms.CharField(label="Fish Caught", max_length=80)

    # Textarea makes the message box bigger than a normal input
    message = forms.CharField(
        label="Message",
        min_length=10,
        max_length=200,
        widget=forms.Textarea
    )

    # The user can only answer Yes or No here
    recommend = forms.ChoiceField(
        label="Would you recommend this location?",
        choices=[
            ("Yes", "Yes"),
            ("No", "No"),
        ]
    )
