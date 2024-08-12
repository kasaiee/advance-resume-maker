from datetime import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

def index(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    return render(request, 'index.html')