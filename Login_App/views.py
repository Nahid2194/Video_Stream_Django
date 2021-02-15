from django.shortcuts import render

# Create your views here.


def signup_user(request):
    return render(request, 'Login_App/signup.html')


def login_user(request):
    return render(request, 'Login_App/login.html')


def logout_user(request):
    return render(request, 'Login_App/signup.html')


def profile(request):
    return render(request, 'Login_App/profile.html')
