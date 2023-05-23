from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=255)
    username = forms.CharField(label="Никнейм на сайте")
    first_name = forms.CharField(label="Имя пользователя (нигде не используется)")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2',)
