from Login_App.models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Email'}))
    password = forms.CharField(required=True, label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Your Password'}))

    class Meta:
        model = User
        fields = ('email', 'password')


class EditProfileForm(models.ModelForm):
    full_name = forms.CharField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Full Name'}))

    class Meta:
        model = Profile
        exclude = ['user']
