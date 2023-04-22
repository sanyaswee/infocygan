from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Article(models.Model):
    user_id = models.IntegerField () #Id, в формі не буде.
    #preview = models.FileField (upload_to = "uploads/") #Фотографія статті
    preview = models.ImageField (upload_to="uploads/", validators = [FileExtensionValidator (allowed_extensions=["webp"])]) #Фотографія статті
    name = models.CharField (max_length = 50, null = False) #Назва посту.
    post = models.TextField (null = False) #Тут має бути ваш пост...
    date =  models.DateTimeField(auto_now=True) #Не треба заповнювати.
