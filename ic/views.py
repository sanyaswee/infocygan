from django.shortcuts import render
from django.http import HttpResponse
from .models import CrEATE_TABlE

# Create your views here.

def index (request):
    if request.method == "GET":
        print ("ABCDE!")
    cREATE_TABlE = CrEATE_TABlE (name = "some")
    
    return render (request, "ic/index.html", {"h1":"Hello!"})