from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from registration.models import UserCustom


# Create your views here.


def index(request):
    return render(request, "home/index.html")


def user_page (request, id):
    if request.user.is_authenticated:
        users = UserCustom.objects.get(id=id)
        return render(request, "home/user_page.html", {"users": users})
    else:
        return redirect ("forbidden")


def forbidden(request):
    if not request.user.is_authenticated:
        return render(request, "home/forbidden.html")
    else:
        return redirect('index')