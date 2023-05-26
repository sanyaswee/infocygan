from django.urls import path
from .views import add_article,view_article

urlpatterns = [
    path ("add/", add_article, name = "add_article"),
    path("view/<a_id>", view_article, name="view_article"),
]