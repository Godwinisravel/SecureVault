from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from vault.models import PasswordEntry, Category

@login_required
def dashboard(request):

    total_passwords = PasswordEntry.objects.filter(
        user=request.user
    ).count()

    favorites = PasswordEntry.objects.filter(
        user=request.user,
        favorite=True
    ).count()

    categories = Category.objects.count()

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "total_passwords": total_passwords,
            "favorites": favorites,
            "categories": categories,
        }
    )