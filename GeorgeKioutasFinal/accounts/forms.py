from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# This form creates a new user and also asks for simple profile details
class RegisterForm(UserCreationForm):
    # These fields are added to Django's ready registration form
    username = forms.CharField(max_length=20)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    # Meta tells the form which database table and fields it uses
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


# This form lets the user update the details given during registration
class ProfileForm(forms.Form):
    # These are the details that a logged in user can change
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
