from django.urls import re_path, path
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('signup/',views.SignUp.as_view(), name="sigup"),
]

