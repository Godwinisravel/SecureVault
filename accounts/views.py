from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm


def home(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})

def dashboard(request):
    return render(request, "dashboard/dashboard.html")