from django import forms


# This section has the form used by the customer during checkout
# This form asks the customer for checkout information
class CheckoutForm(forms.Form):
    # These fields are the simple delivery details for the order
    first_name = forms.CharField(label="First Name", max_length=50)
    last_name = forms.CharField(label="Last Name", max_length=50)
    city = forms.CharField(label="City", max_length=50)
    street_number = forms.CharField(label="Street Number", max_length=50)
    postal_code = forms.CharField(label="Postal Code", max_length=20)

    # The customer chooses one payment method
    payment_method = forms.ChoiceField(
        label="Payment Method",
        # Only two payment choices are needed for this project
        choices=[
            ("Cash", "Cash"),
            ("Card", "Card"),
        ],
        # RadioSelect shows the choices as small circle buttons
        widget=forms.RadioSelect
    )
