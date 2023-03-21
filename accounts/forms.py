from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Login')
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(required=True, label = 'Username', strip=False)
    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(required=True, label='Пароль', strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(required=True, label='Подвердите пароль', strip=False, widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = ('username', 'email', 'password', 'password_confirm','first_name')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
    def clean_first_name(self):
        username = self.cleaned_data.get('username')
        if len(username) < 2:
            raise ValidationError('Username is too short')
        return username