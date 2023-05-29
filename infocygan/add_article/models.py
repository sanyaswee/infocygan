from django.db import models
from django.db.models.functions import Lower

models.CharField.register_lookup(Lower)
models.TextField.register_lookup(Lower)
# from django.core.validators import FileExtensionValidator


# Create your models here.
class Article(models.Model):
    user_id = models.IntegerField(default=1)  # Id, у формі не буде.
    # preview = models.FileField (upload_to = "uploads/") #Фотографія статті
    # preview = models.ImageField(upload_to="uploads/")  # Фотографія статті
    preview_url = models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/e/ea/No_image_preview.png', max_length=300)
    name = models.CharField(max_length=50, null=False, unique=True)  # Назва посту.
    post = models.TextField(null=False)  # Тут має бути ваш пост...
    date = models.DateTimeField(auto_now=True)  # Не треба заповнювати.
