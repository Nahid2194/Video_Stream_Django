from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Login_App.forms import LoginForm, SignupForm, EditProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup_user(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = Profile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Login_App:login'))
    return render(request, 'Login_App/signup.html', context={'form': form})


def login_user(request):
    return render(request, 'Login_App/login.html')


@login_required
def logout_user(request):
    return render(request, 'Login_App/signup.html')


@login_required
def profile(request):
    return render(request, 'Login_App/profile.html')
