from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'surname', 'username', 'password']
