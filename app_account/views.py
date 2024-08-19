from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.conf import settings


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = "registration/signup.html"
