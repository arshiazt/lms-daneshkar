from django import forms

class UserForms(forms.Form):
    email = forms.EmailField(label="Email")