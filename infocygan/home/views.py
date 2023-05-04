from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, "home/index.html")


def forbidden(request):
    if not request.user.is_authenticated:
        return render(request, "home/forbidden.html")
    else:
        return redirect('index')
