from django.db import models

# Create your models here.
class Article(models.Model):
    user_id = models.IntegerField()
    preview = models.FileField(upload_to="uploads/")
    post = models.TextField()
    date =  models.DateTimeField(auto_now=True)
