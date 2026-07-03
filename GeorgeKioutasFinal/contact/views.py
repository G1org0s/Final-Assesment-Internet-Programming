from django import forms
from django.shortcuts import render


# This form is for the contact page.
class ContactForm(forms.Form):
    # These rules are the validation for the contact form.
    name = forms.CharField(label="Name", min_length=2, max_length=30)
    # EmailField checks that the text looks like an email.
    email = forms.EmailField(label="Email", max_length=100)
    subject = forms.CharField(label="Subject", min_length=3, max_length=30)
    # Textarea gives more space for the message.
    message = forms.CharField(
        label="Message",
        min_length=10,
        max_length=200,
        widget=forms.Textarea
    )


# Messages are kept here simple, like the list example in class.
messages_list = []


# This view opens the contact page and checks the contact form.
def contact(request):
    # This text is empty until a message is sent correct.
    message_sent = ""

    # POST means the contact form was submitted.
    if request.method == "POST":
        form = ContactForm(request.POST)

        # Check if the form data is valid before saving it.
        if form.is_valid():
            messages_list.append({
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "subject": form.cleaned_data["subject"],
                "message": form.cleaned_data["message"],
            })
            message_sent = "Your message was sent."
        else:
            # Keep the same page open if the form has mistakes.
            return render(request, "contact/contact.html", {
                "form": form,
                "message_sent": message_sent,
            })
    else:
        # This makes a new empty form when there is no POST.
        form = ContactForm()

    # Send the form and message text to the contact template.
    return render(request, "contact/contact.html", {
        "form": form,
        "message_sent": message_sent,
    })
