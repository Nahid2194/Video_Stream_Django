from Login_App.models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
# signup Form


class SignupForm(UserCreationForm):
    username = forms.CharField(
        required=True, label="",
        widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Email'}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Your Password'}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Your Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': "Username"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfileForm(forms.ModelForm):
    fullname = forms.CharField(
        required=False,
        label="Full name",
    )

    class Meta:
        model = Profile
        exclude = ['user']
