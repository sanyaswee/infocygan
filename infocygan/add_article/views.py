from django.shortcuts import render, redirect
from .form import Form
from .models import Article


# Create your views here.
def add_article(request):
    if request.user.is_authenticated:
        form = Form(request.POST)
        
        print (form.is_valid())
        if form.is_valid ():
            Article.objects.create (**form.cleaned_data)
            redirect ("index")

        return render(request, "add_article/add_article.html", {"form": form})
    else:
        return redirect ('forbidden')
