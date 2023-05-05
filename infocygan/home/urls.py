from django.urls import path
from .views import user_page, index


urlpatterns = [
    path ("", index, name = "index"),
    path ("my/info/", user_page, name = "user_page"),
]