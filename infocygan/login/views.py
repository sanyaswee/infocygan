from django.shortcuts import render
from .forms import LoginForm


# Create your views here.
def login(request):
    return render(request, "login/login.html", {'form': LoginForm})
