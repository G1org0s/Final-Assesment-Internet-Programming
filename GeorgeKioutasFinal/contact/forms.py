from django import forms


# This form is for the contact page
class ContactForm(forms.Form):
    # These rules are the validation for the contact form
    name = forms.CharField(label="Name", min_length=2, max_length=30)

    # EmailField checks that the text looks like an email
    email = forms.EmailField(label="Email", max_length=100)
    subject = forms.CharField(label="Subject", min_length=3, max_length=30)

    # Textarea gives more space for the message
    message = forms.CharField(
        label="Message",
        min_length=10,
        max_length=200,
        widget=forms.Textarea
    )
