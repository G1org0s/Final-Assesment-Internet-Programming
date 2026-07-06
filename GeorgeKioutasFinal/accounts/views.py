from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import LoginForm, ProfileForm, RegisterForm


def check_password_rules(password):
    has_capital = False
    has_number = False
    has_symbol = False

    # This loop checks each character in the password.
    for character in password:
        if character.isupper():
            has_capital = True
        if character.isdigit():
            has_number = True
        if not character.isalnum():
            has_symbol = True

    if len(password) < 8:
        return "Password must have at least 8 characters."
    if not has_capital:
        return "Password must have at least 1 capital letter."
    if not has_number:
        return "Password must have at least 1 number."
    if not has_symbol:
        return "Password must have at least 1 symbol."

    return ""


# This view creates a new user account.
def register(request):
    password_message = ""

    if request.method == "POST":
        form = RegisterForm(request.POST)
        password = request.POST["password1"]
        password_message = check_password_rules(password)

        # Django checks the form before saving the new user.
        if form.is_valid() and password_message == "":
            user = form.save()
            login(request, user)
            return redirect("/profile/")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {
        "form": form,
        "password_message": password_message,
    })


# This view checks the username and password and then logs the user in.
def login_user(request):
    message = ""

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/home/")
            else:
                message = "Wrong username or password."
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {
        "form": form,
        "message": message,
    })


# This view logs out the current user.
def logout_user(request):
    logout(request)
    return redirect("/home/")


# This view shows the profile details of the logged in user.
def profile(request):
    # Only logged in users can open this page.
    if not request.user.is_authenticated:
        return redirect("/login/")

    recent_categories = request.session.get("recent_categories", [])

    return render(request, "accounts/profile.html", {
        "recent_categories": recent_categories,
    })


# This view lets the logged in user change their profile details.
def edit_profile(request):



    
    # Only logged in users can open this page.
    if not request.user.is_authenticated:
        return redirect("/login/")

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]
            user.save()
            return redirect("/profile/")
    else:
        # Initial puts the old user details inside the form.
        form = ProfileForm(initial={
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
        })

    return render(request, "accounts/edit_profile.html", {
        "form": form,
    })


# Dashboard page was removed, so this url opens the home page.
def dashboard(request):
    return redirect("/home/")
