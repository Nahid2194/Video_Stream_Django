from django.shortcuts import render

# Create your views here.


def signup(request):
    return render(request, 'Login_App/signup.html')


def login(request):
    return render(request, 'Login_App/login.html')


def logout(request):
    return render(request, 'Login_App/signup.html')


def profile(request):
    return render(request, 'Login_App/profile.html')
