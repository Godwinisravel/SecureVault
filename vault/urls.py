from django.urls import path
from . import views


urlpatterns = [
    path(
        "vault/",
        views.vault,
        name="vault",
    ),

    path(
        "vault/add/",
        views.add_password,
        name="add_password",
    ),

    path(
        "vault/show/<int:pk>/",
        views.show_password,
        name="show_password",
    ),

    path(
        "vault/edit/<int:pk>/",
        views.edit_password,
        name="edit_password",
    ),

    path(
        "vault/delete/<int:pk>/",
        views.delete_password,
        name="delete_password",
    ),

    path(
        "vault/favorite/toggle/<int:pk>/",
        views.toggle_favorite,
        name="toggle_favorite",
    ),

    path(
        "vault/generate/",
        views.generate_random_password,
        name="generate_password",
    ),

    path(
        "vault/favorites/",
        views.favorites,
        name="favorites",
    ),

    path(
        "vault/categories/",
        views.categories,
        name="categories",
    ),
]