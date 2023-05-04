"""
URL configuration for infocygan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from registration.views import *
from login.views import *
from add_article.views import add_article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('registration/', RegisterView.as_view(), name="registration"),
    path('login/', LoginUserView.as_view(template_name="login/login.html"), name="login"),
    path('logout/', logout_user, name="logout"),
    path("add/", add_article, name="add_article"),
    path("forbidden/", forbidden, name="forbidden"),
]
