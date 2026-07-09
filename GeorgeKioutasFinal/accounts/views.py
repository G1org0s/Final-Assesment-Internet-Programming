from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from .forms import ProfileForm, RegisterForm


def user_can_manage_products(user):
    # Salesmen and Managers can see the custom management button
    if not user.is_authenticated:
        return False

    # filter searches for the group name and exists returns True when it is found
    is_salesman = user.groups.filter(name="Salesmen").exists()
    is_manager = user.groups.filter(name="Managers").exists()

    # One of these two checks must be true
    return is_salesman or is_manager


def check_password_rules(password):
    # These start as false until the correct character is found
    has_capital = False
    has_number = False
    has_symbol = False

    # This loop checks each character in the password
    for character in password:
        if character.isupper():
            has_capital = True
        if character.isdigit():
            has_number = True
        if not character.isalnum():
            has_symbol = True

    # Return the first password rule that was not followed
    if len(password) < 8:
        return "Password must have at least 8 characters."
    if not has_capital:
        return "Password must have at least 1 capital letter."
    if not has_number:
        return "Password must have at least 1 number."
    if not has_symbol:
        return "Password must have at least 1 symbol."

    # An empty message means that every rule was followed
    return ""


# This view creates a new user account
def register(request):
    # This stays empty when the password follows all the rules
    password_message = ""

    # POST means that the user pressed the Register button
    if request.method == "POST":
        # Put the submitted information inside the Django form
        form = RegisterForm(request.POST)
        password = request.POST["password1"]
        password_message = check_password_rules(password)

        # Django checks the form before saving the new user
        if form.is_valid() and password_message == "":
            # form.save adds the new user to the database
            user = form.save()

            # Every new account is placed in the Customers group
            customer_group = Group.objects.get(name="Customers")
            user.groups.add(customer_group)

            # Log in the new user after registration is completed
            login(request, user)
            request.session["can_manage_products"] = False
            return redirect("/profile/")
    else:
        # Show a blank form when the page opens normally
        form = RegisterForm()

    # Send the form and possible password message to the page
    return render(request, "accounts/register.html", {
        "form": form,
        "password_message": password_message,
    })


# This view checks the username and password and then logs the user in
def login_user(request):
    # This message is only filled when the login details are wrong
    message = ""

    if request.method == "POST":
        # AuthenticationForm is Django's ready login form
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            # AuthenticationForm already checked the username and password
            user = form.get_user()
            login(request, user)

            # Keep whether the management button should be shown
            request.session["can_manage_products"] = user_can_manage_products(user)
            return redirect("/home/")
        else:
            message = "Wrong username or password."
    else:
        # Make an empty login form for a normal page visit
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {
        "form": form,
        "message": message,
    })


# This view logs out the current user
def logout_user(request):
    # Django removes the current login session
    logout(request)
    return redirect("/home/")


# This view shows the profile details of the logged in user
def profile(request):
    # Only logged in users can open this page
    if not request.user.is_authenticated:
        return redirect("/login/")

    # Read the last shop category that this user opened
    last_category = request.session.get("last_category", "")

    return render(request, "accounts/profile.html", {
        "last_category": last_category,
    })


# This view lets the logged in user change their profile details
def edit_profile(request):
    # Only logged in users can open this page
    if not request.user.is_authenticated:
        return redirect("/login/")

    if request.method == "POST":
        # Put the submitted profile details in the form
        form = ProfileForm(request.POST)

        if form.is_valid():
            # request.user is the account that is logged in now
            user = request.user

            # Use the checked form values to update the account
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]

            # Save the new profile information in the database
            user.save()
            return redirect("/profile/")
    else:
        # Initial puts the old user details inside the form
        form = ProfileForm(initial={
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
        })

    return render(request, "accounts/edit_profile.html", {
        "form": form,
    })
