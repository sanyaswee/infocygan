from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import  AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView, CreateView



# Create your views here.
# def login(request):
#     return render(request, "login/login.html", {'form': LoginForm})

class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = "login/login.html"

    def get_success_url(self):
        return reverse_lazy("index")

def logout_user(request):
    logout(request)
    return redirect("index")