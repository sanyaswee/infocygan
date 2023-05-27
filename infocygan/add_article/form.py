from django import forms
from .models import Article


class Form(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["name", 'preview_url', "post", 'user_id']
        widgets = {
            "post": forms.Textarea({"placeholder": "Введіть вашу статтю...",
                                    "class": "txtarea"}),
            "name": forms.TextInput({"class": "input"}),
            # "preview": forms.FileInput({"class": "input"})
        }
