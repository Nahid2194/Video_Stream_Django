from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Login_App.forms import LoginForm, SignupForm, EditProfileForm
# Create your views here.


def signup_user(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = Profile(user)
            user_profile.save()
    return render(request, 'Login_App/signup.html', context={'form': form})


def login_user(request):
    return render(request, 'Login_App/login.html')


def logout_user(request):
    return render(request, 'Login_App/signup.html')


def profile(request):
    return render(request, 'Login_App/profile.html')
