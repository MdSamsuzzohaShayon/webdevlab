from django.db import models
from django.utils.text import slugify
from account.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, unique=True)
    content = models.TextField()
    thumbnail = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    link = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Commenter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    commenter = models.ForeignKey(Commenter, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.commenter.name} on {self.article.title}"


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# ArticleTags Table (a junction table to implement many-to-many relationship between Articles and Tags):
class ArticleTags(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
