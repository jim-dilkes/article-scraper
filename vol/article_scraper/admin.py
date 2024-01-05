from django.contrib import admin
from .models import Article, NewsWebsite

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','news_website', 'url')

@admin.register(NewsWebsite)
class NewsWesbiteAdmin(admin.ModelAdmin):
    pass
