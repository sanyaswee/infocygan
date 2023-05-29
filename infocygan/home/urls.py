from django.urls import path
from .views import user_page, IndexView, forbidden, search_post


urlpatterns = [
    path ("", IndexView.as_view(), name = "index"),
    path ("info_user/<id>", user_page, name = "user_page"),
    path ("forbidden/", forbidden, name = "forbidden"),
    path("search/", search_post, name="search_post"),
]