from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Ім\'я', max_length=50)
    last_name = forms.CharField(label='Прізвище', max_length=50)
    username = forms.CharField(label='Нікнейм', min_length=4, max_length=50)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Підтвердіть пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
