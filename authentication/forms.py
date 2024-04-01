from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text="Your email address.")
    username = forms.CharField(help_text="Your desired username.")
    password1 = forms.CharField(widget=forms.PasswordInput, help_text="Enter a password.")
    password2 = forms.CharField(widget=forms.PasswordInput, help_text="Enter the same password as above, for verification.")

    class Meta:

        model = User
        fields = ('email', 'username', 'password1', 'password2') #django default user model password and confirm password are called password1 and password2

