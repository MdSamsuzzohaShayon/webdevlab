from django.contrib import admin
from .models import Tag, ArticleTags, Article, Category, Comment

# Register your models here.

admin.site.register(Tag)
admin.site.register(ArticleTags)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
