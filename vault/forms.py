from django import forms
from .models import PasswordEntry


class PasswordForm(forms.ModelForm):
    class Meta:
        model = PasswordEntry
        fields = [
            "website",
            "url",
            "username",
            "encrypted_password",
            "category",
            "notes",
            "favorite",
        ]

        widgets = {
            "encrypted_password": forms.PasswordInput(),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }