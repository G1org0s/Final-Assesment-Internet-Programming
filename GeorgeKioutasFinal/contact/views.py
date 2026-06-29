from django.shortcuts import render

# This view opens the contact page.
def contact(request):
    return render(request, "contact/contact.html")
