from django.shortcuts import render
from .forms import ContactForm




# This section keeps the simple contact messages while the server is running
# Messages are kept here simple, like the list example in class.
messages_list = []




# This section opens the contact page and checks the submitted contact form





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
