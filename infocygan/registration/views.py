# from django.shortcuts import render
# from .forms import RegistrationForm


# Create your views here.
# def registration(request):
#     return render(request, 'registration/register.html', {'form': RegistrationForm})
from django.views.generic import CreateView
from .forms import RegistrationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import  AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.views.generic import ListView, CreateView



class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = "registration/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("index")
