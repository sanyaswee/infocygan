from django import forms
from .models import Article

class Form (forms.ModelForm):
    class Meta:
        model = Article
        fields = ["name", "preview", "post"]
        widgets = {
            "post": forms.Textarea({"placeholder":"Введіть вашу статтю..."})
        }