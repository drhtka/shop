from django.contrib import admin
from articles.models import Article
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'date', 'author',)
    list_filter = ('title', 'id', 'date', 'author',)

admin.site.register(Article, ArticlesAdmin)
