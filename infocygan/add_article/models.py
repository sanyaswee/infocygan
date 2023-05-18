from django.db import models
# from django.core.validators import FileExtensionValidator


# Create your models here.
class Article(models.Model):
    user_id = models.IntegerField(default=1)  # Id, в формі не буде.
    # preview = models.FileField (upload_to = "uploads/") #Фотографія статті
    # preview = models.ImageField(upload_to="uploads/")  # Фотографія статті
    name = models.CharField(max_length=50, null=False, unique=True)  # Назва посту.
    post = models.TextField(null=False)  # Тут має бути ваш пост...
    date = models.DateTimeField(auto_now=True)  # Не треба заповнювати.
