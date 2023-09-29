from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'text_input auth'}),
            'password': forms.TextInput(attrs={'class': 'text_input auth', 'type': 'password'}),
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'text_input auth'}),
            'email': forms.TextInput(attrs={'class': 'text_input auth'}),
            'first_name': forms.TextInput(attrs={'class': 'text_input auth'}),
            'last_name': forms.TextInput(attrs={'class': 'text_input auth'}),
            # 'password1': forms.TextInput(attrs={'class': 'text_input auth', 'type': 'password'}),
            # 'password2': forms.TextInput(attrs={'class': 'text_input auth', 'type': 'password'}),
        }
