from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy


# Create your views here.
# def login(request):
#     return render(request, "login/login.html", {'form': LoginForm})

class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = "login/login.html"

    def get_success_url(self):
        return reverse_lazy("index")


def logout_user(request):
    logout(request)
    return redirect("forbidden")