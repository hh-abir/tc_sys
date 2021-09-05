from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']
        widgets = {
            "username": forms.TextInput(attrs = {"class": "input100", "placeholder": "Username..."}),
            "email": forms.EmailInput(attrs = {"class": "input100", "placeholder": "Email..."}),
            "passowrd1": forms.PasswordInput(attrs = {"class": "input100", "placeholder": "Password"}),
            "password2": forms.PasswordInput(attrs = {"class": "input100", "placeholder": "Retype Password"}),
        }