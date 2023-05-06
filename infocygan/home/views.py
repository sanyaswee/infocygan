from django.shortcuts import render, redirect

# Create your views here.
from .models import *


def index(request):
    return render(request, "home/index.html")

def user_page (request):
    if request.user.is_authenticated:
        users = request.user
        return render(request, "home/user_page.html", {"users": users})
    else:
        return redirect ("registration")