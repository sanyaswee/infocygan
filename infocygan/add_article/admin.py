from django.contrib import admin
from .models import Article
# Register your models here.
class ArticleAdmin (admin.ModelAdmin):
    list_display = ["user_id","name", "post", "date"]
    search_fields = ["name"]

admin.site.register (Article, ArticleAdmin)