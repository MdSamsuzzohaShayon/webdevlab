import graphene
from .queryTypes import CategoryType, ArticleType, CommentType, TagType, CommenterType, AuthorType
from ..models import Category, Article, Comment, Tag, Commenter
from account.models import User

class Query(graphene.ObjectType):

    all_authors = graphene.List(AuthorType)
    all_categories = graphene.List(CategoryType)
    all_articles = graphene.List(ArticleType, start=graphene.Int(), limit=graphene.Int())
    all_comments = graphene.List(CommentType)
    all_commenters = graphene.List(CommenterType)
    all_tags = graphene.List(TagType)

    author_by_id = graphene.Field(AuthorType, id=graphene.Int())
    commenter_by_id = graphene.Field(AuthorType, id=graphene.Int())
    category_by_id = graphene.Field(CategoryType, id=graphene.Int())
    article_by_id = graphene.Field(ArticleType, id=graphene.Int())
    article_by_link = graphene.Field(ArticleType, link=graphene.String())
    # comment_by_id = graphene.Field(CommentType, id=graphene.Int())
    # tag_by_id = graphene.Field(TagType, id=graphene.Int())

    def resolve_all_authors(self, info):
        return User.objects.all()

    def resolve_all_categories(self, info):
        objects = Category.objects.all().order_by('-id')
        return objects

    def resolve_all_articles(self, info, start: int=0, limit: int=20):
        # Get all objects in reverse order
        queryset = Article.objects.all().order_by('-id')
        # Apply start and limit using array slicing
        objects = queryset[start:start + limit]
        return objects

    def resolve_all_comments(self, info):
        objects = Comment.objects.all().order_by('-id')
        return objects

    def resolve_all_commenters(self, info):
        objects = Commenter.objects.all().order_by('-id')
        return objects

    def resolve_commenter_by_id(self, info, id):
        return Commenter.objects.get(pk=id)

    def resolve_all_tags(self, info):
        return Tag.objects.all()

    def resolve_author_by_id(self, info, id):
        return User.objects.get(pk=id)

    def resolve_category_by_id(self, info, id):
        return Category.objects.get(pk=id)

    def resolve_article_by_id(self, info, id):
        return Article.objects.get(pk=id)

    def resolve_article_by_link(self, info, link):
        return Article.objects.get(link=link)

    # def resolve_comment_by_id(self, info, id):
    #     return Comment.objects.get(pk=id)

    # def resolve_tag_by_id(self, info, id):
    #     return Tag.objects.get(pk=id)

