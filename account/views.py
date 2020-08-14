from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(reverse('map:main'))
        else:
            return render(request, "account/login.html", {'error': 'username or password is incorrect'})
    else:
        return render(request, "account/login.html")


def logout(request):
    auth.logout(request)
    return redirect("map:main")
