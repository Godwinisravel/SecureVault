from django import forms
from .models import PasswordEntry


class PasswordForm(forms.ModelForm):

    class Meta:
        model = PasswordEntry

        fields = [
            "website",
            "url",
            "username",
            "password",
            "category",
            "notes",
            "favorite",
        ]

        widgets = {
            "website": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Website name",
                }
            ),

            "url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com",
                }
            ),

            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Username or email",
                }
            ),

            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter password",
                    "autocomplete": "new-password",
                }
            ),

            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Additional notes",
                    "rows": 4,
                }
            ),

            "favorite": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }