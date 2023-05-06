from django.urls import path
from .views import add_article

urlpatterns = [
    path ("add/", add_article, name = "add_article")
]