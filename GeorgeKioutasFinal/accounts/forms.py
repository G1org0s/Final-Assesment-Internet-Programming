from django import forms
from django.contrib.auth.forms import AuthenticationForm


# This section has the forms for user registration, login and profile editing



# This form creates a new user and also asks for simple profile details
class RegisterForm(forms.Form):
    # These are the details that the new user writes
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50, required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password1 = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", max_length=50, widget=forms.PasswordInput)


# This is Django's login form, but the username is limited to 30 characters
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


# This form lets the user update the details given during registration
class ProfileForm(forms.Form):
    # These are the details that a logged in user can change
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
