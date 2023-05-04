from django.shortcuts import render, redirect
from .form import Form


# Create your views here.
def add_article(request):
    if request.user.is_authenticated:
        form = Form(request.POST)
        return render(request, "add_article/add_article.html", {"form": form})
    else:
        return redirect('forbidden')
