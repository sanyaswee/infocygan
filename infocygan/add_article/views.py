from django.shortcuts import render
from .form import Form

# Create your views here.
def add_article (request):
    form = Form (request.POST)
    return render (request, "add_article/add_article.html", {"form":form})