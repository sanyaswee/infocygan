from django.urls import path
from .views import LoginUserView, logout_user

urlpatterns = [
    path('login/', LoginUserView.as_view(template_name="login/login.html"), name="login"),
    path('logout/', logout_user, name="logout"),
]