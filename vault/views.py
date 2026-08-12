from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q

from .forms import PasswordForm
from .models import PasswordEntry, Category
from .services.generator import generate_password


@login_required
def add_password(request):

    if request.method == "POST":

        form = PasswordForm(request.POST)

        if form.is_valid():

            entry = form.save(commit=False)

            entry.user = request.user

            entry.save()

            return redirect("vault")

    else:

        form = PasswordForm()

    return render(
        request,
        "vault/add_password.html",
        {
            "form": form
        }
    )


@login_required
def vault(request):

    query = request.GET.get("q", "").strip()

    passwords = PasswordEntry.objects.filter(
        user=request.user
    )

    if query:

        passwords = passwords.filter(
            Q(website__icontains=query)
            | Q(username__icontains=query)
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

    entry = get_object_or_404(
        PasswordEntry,
        pk=pk,
        user=request.user
    )

    return JsonResponse(
        {
            "password": entry.password
        }
    )


@login_required
def edit_password(request, pk):

    entry = get_object_or_404(
        PasswordEntry,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        form = PasswordForm(
            request.POST,
            instance=entry
        )

        if form.is_valid():

            form.save()

            return redirect("vault")

    else:

        form = PasswordForm(
            instance=entry
        )

    return render(
        request,
        "vault/edit_password.html",
        {
            "form": form,
            "entry": entry,
        }
    )


@login_required
def delete_password(request, pk):

    entry = get_object_or_404(
        PasswordEntry,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        entry.delete()

    return redirect("vault")


@login_required
def toggle_favorite(request, pk):

    entry = get_object_or_404(
        PasswordEntry,
        pk=pk,
        user=request.user
    )

    entry.favorite = not entry.favorite

    entry.save(
        update_fields=["favorite"]
    )

    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "vault"
        )
    )


@login_required
def generate_random_password(request):

    password = generate_password()

    return JsonResponse(
        {
            "password": password
        }
    )


@login_required
def favorites(request):

    passwords = PasswordEntry.objects.filter(
        user=request.user,
        favorite=True
    ).order_by("website")

    return render(
        request,
        "vault/favorites.html",
        {
            "passwords": passwords
        }
    )


@login_required
def categories(request):

    categories = Category.objects.filter(
        user=request.user
    ).prefetch_related(
        "passwordentry_set"
    )

    return render(
        request,
        "vault/categories.html",
        {
            "categories": categories
        }
    )