from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('SignUp',views.SignUp, name='SignUp'),
    path('Login',views.Login, name='Login'),
    path('SignOut',views.SignOut, name='SignOut'),
]