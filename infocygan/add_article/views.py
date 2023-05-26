from django.shortcuts import render, redirect
from .form import Form
from .models import Article
from django.http import Http404
from registration.models import UserCustom


# Create your views here.
def add_article(request):
    if request.user.is_authenticated:
        form = Form(request.POST)
        print(form.is_valid())
        if form.is_valid():
            # form.user_id = int(request.user.id)
            # print(form.user_id)
            # form.save()
            print(form.cleaned_data)
            Article.objects.create(**form.cleaned_data)
            return redirect("index")
        return render(request, "add_article/add_article.html", {"form": form})
    else:
        return redirect('forbidden')

def view_article(request, a_id):
    try:
        article = Article.objects.get(id=a_id)
        author = UserCustom.objects.get(id=article.user_id)
        print(author)
    except:
        raise Http404
    print(article)
    return render(request, "add_article/article_page.html", {"article":article, "author":author})
