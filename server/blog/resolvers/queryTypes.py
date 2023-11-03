from graphene_django.types import DjangoObjectType
from ..models import Author, Category, Article, Comment, Tag

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class TagType(DjangoObjectType):
    class Meta:
        model = Tag