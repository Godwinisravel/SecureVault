from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PasswordEntry(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    website = models.CharField(max_length=200)

    url = models.URLField(blank=True)

    username = models.CharField(max_length=200)

    encrypted_password = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    notes = models.TextField(blank=True)

    favorite = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website