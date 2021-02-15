from django.contrib import admin
from django.urls import path
from Login_App import views


app_name = 'Login_App'

urlpatterns = [
    path('signup/', views.signup_user, name="signup"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/', views.profile, name="profile"),
]
