from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from registration.models import UserCustom
from add_article.models import Article
from django.views.generic import ListView

class IndexView(ListView):
    model = Article
    template_name = "home/index.html"
    context_object_name = "articles"
    paginate_by = 5
    def get_queryset(self):
        return Article.objects.all()


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