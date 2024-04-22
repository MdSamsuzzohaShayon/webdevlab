from graphene_django.types import DjangoObjectType
from ..models import Category, Article, Comment, Tag, Commenter
from account.models import User


class CommenterType(DjangoObjectType):
    class Meta:
        model = Commenter


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
