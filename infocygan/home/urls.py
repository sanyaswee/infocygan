from django.urls import path
from .views import user_page, index, forbidden


urlpatterns = [
    path ("", index, name = "index"),
    path ("my/info/", user_page, name = "user_page"),
    path ("forbidden/", forbidden, name = "forbidden"),
]