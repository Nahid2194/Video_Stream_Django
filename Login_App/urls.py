from django.contrib import admin
from django.urls import path
from Login_App import views


app_name = 'Login_App'

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]
