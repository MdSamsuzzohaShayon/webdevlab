import graphene
from graphene_django import DjangoObjectType
from ..models import Category, Article, Comment
from .queryTypes import CategoryType, ArticleType, CommentType
from core.settings import cloudinary
from graphene_file_upload.scalars import Upload
from datetime import datetime
import os


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
        thumbnail = Upload(required=True)
        author_id = graphene.ID()
        category_id = graphene.ID()
        created_at = graphene.DateTime(required=False)
        id = graphene.ID()

    success = graphene.Boolean()
    article = graphene.Field(ArticleType)

    @classmethod
    def mutate(cls, root, info, title, content, thumbnail, author_id, category_id, created_at=None, id=None):

        # Upload the image to Cloudinary
        options = {
            'folder': os.environ["CLOUDINARY_FOLDER_NAME"],
            "width": 300, "height": 300, "crop": "thumb"
        }
        cloudinary_response = cloudinary.uploader.upload(thumbnail, **options)

        # Get the URL of the uploaded image from the Cloudinary response
        thumbnail_url = cloudinary_response['public_id']
        # print({"thumbnail_url": thumbnail_url, "cloudinary_response": cloudinary_response})
        # result  = {'thumbnail_url': 'http://res.cloudinary.com/shayon-cloud/image/upload/v1703304728/kd1pcwdt1vyuzqoqmmst.jpg', 'cloudinary_response': {'asset_id': 'bc854fde83711cb4b1983764e884d7e0', 'public_id': 'kd1pcwdt1vyuzqoqmmst', 'version': 1703304728, 'version_id': '0cef85e7ba27804a7c6609db55035c20', 'signature': 'e12e6a78d6f4366f5cfba4da278df3c92b6f7b62', 'width': 3081, 'height': 4622, 'format': 'jpg', 'resource_type': 'image', 'created_at': '2023-12-23T04:12:08Z', 'tags': [], 'bytes': 506228, 'type': 'upload', 'etag': '400efc41ef8dc16183220bfa335a4b7e', 'placeholder': False, 'url': 'http://res.cloudinary.com/shayon-cloud/image/upload/v1703304728/kd1pcwdt1vyuzqoqmmst.jpg', 'secure_url': 'https://res.cloudinary.com/shayon-cloud/image/upload/v1703304728/kd1pcwdt1vyuzqoqmmst.jpg', 'folder': '', 'original_filename': 'pexels-blue-record-19397385', 'api_key': '455739236686664'}}

        # Get the current date and time
        current_date_time = datetime.now()

        if id:
            article = Article.objects.get(pk=id)
            article.title = title
            article.content = content
            article.thumbnail = thumbnail_url
            article.created_at = current_date_time
            if author_id:
                article.author_id = author_id
            if category_id:
                article.category_id = category_id
            article.save()
        else:
            article = Article.objects.create(title=title, content=content, thumbnail=thumbnail_url,
                                             created_at=current_date_time, author_id=author_id,
                                             category_id=category_id)
        return ArticleMutation(article=article)


class CommentMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        author = graphene.String(required=True)  # Who made the comment
        email = graphene.String(required=True)
        text = graphene.String(required=True)
        created_at = graphene.DateTime(required=False)
        article_id = graphene.ID()

    comment = graphene.Field(CommentType)

    @classmethod
    def mutate(cls, root, info, author, email, text, article_id, created_at=None, id=None):
        current_date_time = datetime.now()
        if id:
            comment = Comment.objects.get(pk=id)
            comment.author = author
            comment.created_at = current_date_time
            comment.text = text
            comment.email = email
            if article_id:
                comment.article_id = article_id
            comment.save()
        else:
            comment = Comment.objects.create(author=author, email=email, text=text, article_id=article_id,
                                             created_at=current_date_time)
        return CommentMutation(comment=comment)


class Mutation(graphene.ObjectType):
    create_or_update_category = CategoryMutation.Field()
    create_or_update_article = ArticleMutation.Field()
    create_or_update_comment = CommentMutation.Field()
