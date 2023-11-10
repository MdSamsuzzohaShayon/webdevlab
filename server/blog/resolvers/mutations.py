import graphene
from graphene_django import DjangoObjectType
from ..models import Category, Article
from .queryTypes import CategoryType, ArticleType


class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id=None):
        if id:
            category = Category.objects.get(pk=id)
            category.name = name
            category.save()
        else:
            category = Category.objects.create(name=name)
        return CategoryMutation(category=category)


class ArticleMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        created_at = graphene.Date()
        author_id = graphene.ID()
        category_id = graphene.ID()
        id = graphene.ID()

    article = graphene.Field(ArticleType)

    @classmethod
    def mutate(cls, root, info, title, content, created_at, author_id, category_id, id=None):
        if id:
            article = Article.objects.get(pk=id)
            article.title = title
            article.content = content
            if created_at:
                article.created_at = created_at
            if author_id:
                article.author_id = author_id
            if category_id:
                article.category_id = category_id
            article.save()
        else:
            article = Article.objects.create(title=title, content=content, created_at=created_at, author_id=author_id,
                                             category_id=category_id)
        return ArticleMutation(article=article)


class Mutation(graphene.ObjectType):
    create_or_update_category = CategoryMutation.Field()
    create_or_update_article = ArticleMutation.Field()
