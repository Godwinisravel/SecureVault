from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import PasswordForm
from .models import PasswordEntry
from django.http import JsonResponse
from .services.encryption import decrypt_password
from .services.encryption import encrypt_password
from django.http import JsonResponse
from .services.generator import generate_password

@login_required
def add_password(request):

    if request.method == "POST":

        form = PasswordForm(request.POST)

        if form.is_valid():

            password = form.cleaned_data["encrypted_password"]

            obj = form.save(commit=False)

            obj.user = request.user

            obj.encrypted_password = encrypt_password(password)

            obj.save()

            return redirect("vault")

    else:

        form = PasswordForm()

    return render(
        request,
        "vault/add_password.html",
        {"form": form},
    )

@login_required
def edit_password(request, pk):

    entry = PasswordEntry.objects.get(
        id=pk,
        user=request.user
    )

    if request.method == "POST":

        form = PasswordForm(request.POST, instance=entry)

        if form.is_valid():

            obj = form.save(commit=False)

            password = form.cleaned_data["encrypted_password"]

            obj.encrypted_password = encrypt_password(password)

            obj.save()

            return redirect("vault")

    else:

        form = PasswordForm(instance=entry)

        form.initial["encrypted_password"] = decrypt_password(
            entry.encrypted_password
        )

    return render(
        request,
        "vault/edit_password.html",
        {
            "form": form
        }
    )

from django.db.models import Q

@login_required
def vault(request):

    query = request.GET.get("q", "")

    passwords = PasswordEntry.objects.filter(
        user=request.user
    )

    if query:

        passwords = passwords.filter(
            Q(website__icontains=query) |
            Q(username__icontains=query)
        )

    passwords = passwords.order_by("website")

    return render(
        request,
        "vault/vault.html",
        {
            "passwords": passwords,
            "query": query,
        }
    )


@login_required
def show_password(request, pk):

    try:
        entry = PasswordEntry.objects.get(
            id=pk,
            user=request.user
        )

        return JsonResponse({
            "password": decrypt_password(entry.encrypted_password)
        })

    except PasswordEntry.DoesNotExist:

        return JsonResponse({
            "error": "Password not found"
        }, status=404)

@login_required
def delete_password(request, pk):

    entry = PasswordEntry.objects.get(
        id=pk,
        user=request.user
    )

    entry.delete()

    return redirect("vault")

@login_required
def generate_random_password(request):

    password = generate_password()

    return JsonResponse({
        "password": password
    })

@login_required
def favorites(request):

    passwords = PasswordEntry.objects.filter(
        user=request.user,
        favorite=True
    )

    return render(
        request,
        "vault/favorites.html",
        {
            "passwords": passwords
        }
    )

from .models import Category

@login_required
def categories(request):

    categories = Category.objects.all().prefetch_related("passwordentry_set")

    return render(
        request,
        "vault/categories.html",
        {
            "categories": categories
        }
    )