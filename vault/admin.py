from django.contrib import admin
from .models import Category, PasswordEntry

admin.site.register(Category)
admin.site.register(PasswordEntry)