import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from mixer.backend.django import mixer
from graphene.test import Client
from core.schema import schema
from account.models import User
from blog.models import Category, Article, Comment, Tag
from django.test import TestCase



@pytest.fixture
def graphql_client():
    return Client(schema)

@pytest.fixture
def setup_test_environment():
    # Setup test environment (e.g., populate database)
    users = mixer.cycle(5).blend(User)  # Create 5 test users
    categories = mixer.cycle(3).blend(Category)  # Create 3 test categories
    articles = mixer.cycle(10).blend(Article)  # Create 10 test articles
    comments = mixer.cycle(7).blend(Comment)  # Create 7 test comments
    tags = mixer.cycle(4).blend(Tag)  # Create 4 test tags
    yield  # This is where the test will execute
    # Teardown test environment (not necessary in this case)


def test_all_authors(graphql_client):
    # Create test users using mixer
    mixer.cycle(5).blend(User)

    # Execute the query
    executed = graphql_client.execute('''
    query GetAuthors{
          allAuthors{
                id
                username
                email
          }
    }
    ''')

    # Check the result
    assert 'errors' not in executed
    # assert len(executed['data']['allAuthors']) == 5


def test_all_categories(graphql_client):
    # Create test categories using mixer
    mixer.cycle(3).blend(Category)

    # Execute the query
    executed = graphql_client.execute('''
    query {
        allCategories {
            id
            name
        }
    }
    ''')

    # Check the result
    assert 'errors' not in executed
    # assert len(executed['data']['allCategories']) == 3


def test_all_articles(graphql_client):
    # Create test articles using mixer
    mixer.cycle(10).blend(Article)

    # Execute the query
    executed = graphql_client.execute('''
    query {
        allArticles(start: 0, limit: 5) {
            id
            title
        }
    }
    ''')

    # Check the result
    assert 'errors' not in executed
    # assert len(executed['data']['allArticles']) == 10


def test_all_comments(graphql_client):
    # Create test comments using mixer
    mixer.cycle(7).blend(Comment)

    # Execute the query
    executed = graphql_client.execute('''
    query {
        allComments {
            id
            text
        }
    }
    ''')

    # Check the result
    assert 'errors' not in executed
    # assert len(executed['data']['allComments']) == 7


def test_all_tags(graphql_client):
    # Create test tags using mixer
    mixer.cycle(4).blend(Tag)

    # Execute the query
    executed = graphql_client.execute('''
    query {
        allTags {
            id
            name
        }
    }
    ''')

    # Check the result
    assert 'errors' not in executed
    # assert len(executed['data']['allTags']) == 4


def test_author_by_id(graphql_client):
    # Create a test user using mixer
    user = mixer.blend(User)

    # Execute the query
    executed = graphql_client.execute('''
    query GetAuthorById{
      authorById(id: %d){
        id
        username
        email
      }
    }
    ''' % user.id)

    # Check the result
    assert 'errors' not in executed
    assert executed['data']['authorById']['id'] == str(user.id)
    # assert executed['data']['authorById']['name'] == user.commentor


def test_category_by_id(graphql_client):
    # Create a test category using mixer
    category = mixer.blend(Category)

    # Execute the query
    executed = graphql_client.execute('''
    query {
        categoryById(id: %d) {
            id
            name
        }
    }
    ''' % category.id)

    # Check the result
    assert 'errors' not in executed
    assert executed['data']['categoryById']['id'] == str(category.id)
    assert executed['data']['categoryById']['name'] == category.name

# Similarly, write tests for article_by_id, article_by_link, and other queries as needed
# https://stackoverflow.com/questions/6049933/django-import-error-no-module-named-core-management
