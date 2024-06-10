import json 
from core.settings import cloudinary
from graphene.test import Client
from core.schema import schema  # Import your GraphQL schema
from account.models import User
from django.contrib.auth.models import AnonymousUser
from blog.models import Category, Article, Comment, Commenter
from datetime import datetime
from django.db.utils import IntegrityError
import random
from random import randint
from tabulate import tabulate


def cleanup_database():
    # Delete all existing records from relevant tables
    User.objects.all().delete()
    Category.objects.all().delete()
    Article.objects.all().delete()
    Comment.objects.all().delete()
    Commenter.objects.all().delete()

def seed_users():
    # Seed the database with three users
    for i in range(3):
        email = f"ex-user{i+1}@wdl.com"
        password = "password123"
        first_name = f"User{i+1}"
        last_name = "Doe"

        # Create user directly using Django ORM
        user = User.objects.create(
            email=email,
            username=email,
            first_name=first_name,
            last_name=last_name,
            is_active=True  # Assuming all seeded users are active
        )

        # Set password using make_password to hash the password
        user.set_password(password)
        user.save()

        print(f"User {i+1} created with ID: {user.id}")

def verify_users():
    # Verify all the users
    users = User.objects.all()
    for user in users:
        user.is_active = True
        user.save()


def login_and_get_tokens():
    # Log in each user and get their tokens
    for i in range(3):
        email = f"ex-user{i+1}@wdl.com"
        password = "password123"
        login_mutation = '''
            mutation {
                login(email: "%s", password: "%s") {
                    user{
                      id
                      email
                      firstName
                      lastName
                    }
                    accessToken
                    refreshToken
                }
            }
        ''' % (email, password)
        client = Client(schema)
        result = client.execute(login_mutation, context_value={'request': None, 'user': AnonymousUser()})
        access_token = result['data']['login']['accessToken']
        refresh_token = result['data']['login']['refreshToken']
        user = result['data']['login']['user']
        print(f"User {i+1} logged in:")
        print(f"Access Token: {access_token}")
        print(f"Refresh Token: {refresh_token}")
        print(f"User: {user}")



def seed_data():
    # Create and verify users
    users = User.objects.all()[:3]  # Assuming you have at least 3 verified users

    # Create 5 categories (Tech category)
    # categories = []
    # for i in range(5):
    #     category = Category.objects.create(name=f"Tech category {i + 1}")
    #     categories.append(category)
    category_news = Category.objects.create(name=f"News")
    category_tutorial = Category.objects.create(name=f"Tutorial")
    category_trending = Category.objects.create(name=f"Trending")
    category_latest = Category.objects.create(name=f"Latest")
    categories = [category_news, category_tutorial, category_trending, category_latest]


    commenters = []
    for i in range(10):
        commenter = Commenter.objects.create(
            name=f"Commenter {i + 1}",
            email=f"commenter{i + 1}@wdl.com"
        )
        commenters.append(commenter)

    # Upload thumbnail and save public ID for each article
    articles_data = []
    json_data = None 
    with open('blog_data.json', 'r') as blog_data_file:
        json_data = json.load(blog_data_file)

    if json_data:
        for item in json_data:
            random_pic = randint(1, 10)
            article_element = {
                "title": item['title'],
                "content": item['content'],
                "thumbnail": f"static/{random_pic:02d}.webp",
                "category_id": random.choice(categories).id,
                "author_id": random.choice(users).id
            }
            articles_data.append(article_element)

    for article_data in articles_data:
        try:
            category_id = article_data.pop("category_id")
            author_id = article_data.pop("author_id")
            category = Category.objects.get(pk=category_id)
            author = User.objects.get(pk=author_id)

            # Upload thumbnail to Cloudinary
            thumbnail_path = article_data.pop("thumbnail")
            thumbnail_upload_response = cloudinary.uploader.upload(thumbnail_path)

            # Get the public ID of the uploaded thumbnail
            thumbnail_url = thumbnail_upload_response['public_id']

            # Add thumbnail URL to article data
            article_data["thumbnail"] = thumbnail_url

            article_data["category"] = category
            article_data["author"] = author
            article = Article.objects.create(**article_data)

            # Randomly determine the number of comments for each article
            num_comments = random.randint(0, 5)
            for _ in range(num_comments):
                commenter = random.choice(commenters)
                Comment.objects.create(
                    article=article,
                    commenter=commenter,
                    text="This is a sample comment."
                )

        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            # Handle the integrity error, e.g., log the error or skip the creation of the problematic record
            pass

def display_data():
    # Fetch data from all relevant models
    users = User.objects.all()
    categories = Category.objects.all()
    articles = Article.objects.all()
    comments = Comment.objects.all()

    # Format data into tables
    user_data = [[user.id, user.first_name, user.last_name, user.email] for user in users]
    category_data = [[category.id, category.name] for category in categories]
    article_data = [[
        article.id,
        article.title,
        article.content,
        article.thumbnail,
        article.category.name,
        f"{article.author.first_name} {article.author.last_name}"
    ] for article in articles]
    comment_data = [[comment.id, comment.text, comment.article.title] for comment in comments]

    # Define headers for each table
    user_headers = ["ID", "First Name", "Last Name", "Email"]
    category_headers = ["ID", "Name"]
    article_headers = ["ID", "Title", "Content", "Thumbnail", "Category", "Author"]
    comment_headers = ["ID", "Content", "Article Title"]

    # Display tables
    print("Users:")
    print(tabulate(user_data, headers=user_headers, tablefmt="grid"))
    print("\nCategories:")
    print(tabulate(category_data, headers=category_headers, tablefmt="grid"))
    print("\nArticles:")
    print(tabulate(article_data, headers=article_headers, tablefmt="grid"))
    print("\nComments:")
    print(tabulate(comment_data, headers=comment_headers, tablefmt="grid"))

# Terminal commands
# ./manage.py shell

"""
./manage.py shell
>>> from blog_seed import cleanup_database, seed_users, verify_users, login_and_get_tokens, seed_data
>>> cleanup_database()
>>> seed_users()
>>> verify_users()
>>> login_and_get_tokens()
>>> seed_data()
"""

def init():
    cleanup_database()
    seed_users()
    verify_users()
    login_and_get_tokens()
    seed_data()
    display_data()
