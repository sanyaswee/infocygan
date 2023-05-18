from django.db import models
from django.contrib.auth.models import User

class UserCustom(User):
    # user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    logo = models.ImageField(default=None)
    USERNAME_FIELD = 'username'