from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserRegisterForm(UserCreationForm):

    phone = forms.CharField(max_length=11)
    class Meta:
        model = User
        fields = ['first_name','last_name','phone','password1','password2']

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(max_length=11)
    password = forms.CharField(max_length=128)
