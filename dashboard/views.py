from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from vault.models import PasswordEntry, Category


@login_required
def dashboard(request):

    # Current logged-in user
    user = request.user

    # Count this user's passwords
    total_passwords = PasswordEntry.objects.filter(
        user=user
    ).count()

    # Count this user's favorite passwords
    favorites = PasswordEntry.objects.filter(
        user=user,
        favorite=True
    ).count()

    # Count this user's categories
    categories = Category.objects.filter(
        user=user
    ).count()

    context = {
        "total_passwords": total_passwords,
        "favorites": favorites,
        "categories": categories,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )