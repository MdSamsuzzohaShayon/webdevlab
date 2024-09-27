import json
import pytest
from PIL import Image
from graphene_django.utils.testing import graphql_query
from django.test import Client
from io import BytesIO
from requests_toolbelt import MultipartEncoder

def create_fake_image():
    image = Image.new('RGB', (100, 100), color=(73, 109, 137))
    byte_arr = BytesIO()
    image.save(byte_arr, format='JPEG')
    byte_arr.seek(0)
    return byte_arr

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func

def test_category_mutation(client_query):
    mutation = '''
        mutation CreateOrUpdateCategory{
          createOrUpdateCategory(name: "New Category - 1"){
            category{
              id
              name
            }
          }
        }
    '''

    response = client_query(mutation, op_name='CreateOrUpdateCategory')
    content = json.loads(response.content)
    assert 'errors' not in content
    # Additional assertions based on expected behavior
    assert 'data' in content
    data = content['data']
    assert 'createOrUpdateCategory' in data
    category_data = data['createOrUpdateCategory']
    assert 'category' in category_data
    category = category_data['category']
    assert 'id' in category
    assert 'name' in category
    assert category['name'] == "New Category - 1"
    assert category['id'] is not None


def create_multipart_form_data(file_data, file_name, content_type):
    """
    Create a multipart/form-data payload with the provided file data.
    """
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    form_data = BytesIO()
    form_data.write(f"--{boundary}\r\n".encode())
    form_data.write(f'Content-Disposition: form-data; name="operations"\r\n\r\n'.encode())
    form_data.write(json.dumps({
        "query": "mutation ($file: Upload!) { uploadFile(file: $file) { id } }",
        "variables": {
            "file": None  # Placeholder for file data
        }
    }).encode())
    form_data.write(f"\r\n--{boundary}\r\n".encode())
    form_data.write(f'Content-Disposition: form-data; name="map"\r\n\r\n'.encode())
    form_data.write(json.dumps({
        "0": ["variables.file"]
    }).encode())
    form_data.write(f"\r\n--{boundary}\r\n".encode())
    form_data.write(f'Content-Disposition: form-data; name="0"; filename="{file_name}"\r\n'.encode())
    form_data.write(f"Content-Type: {content_type}\r\n\r\n".encode())
    form_data.write(file_data)
    form_data.write(f"\r\n--{boundary}--\r\n".encode())
    form_data.seek(0)

    return form_data

def test_article_mutation(client_query):
    fake_image = create_fake_image()

    mutation = '''
        mutation CreateOrUpdateArticle($title: String!, $content: String!, $thumbnail: Upload!, $authorId: ID!, $categoryId: ID) {
            createOrUpdateArticle(
                title: $title,
                content: $content,
                thumbnail: $thumbnail,
                authorId: $authorId,
                categoryId: $categoryId
            ) {
                article {
                    id
                    title
                    content
                    thumbnail
                }
            }
        }
    '''

    variables = {
        'title': "New Article",
        'content': "Article content...",
        'thumbnail': None,
        'authorId': 5,
        'categoryId': 5
    }

    operations = json.dumps({
        'query': mutation,
        'variables': variables
    })

    map_data = json.dumps({
        '0': ['variables.thumbnail']
    })

    # Create a multipart form data payload
    form_data = MultipartEncoder(
        fields={
            'operations': operations,
            'map': map_data,
            '0': ('test_image.jpg', fake_image, 'image/jpeg')
        }
    )

    client = Client()
    response = client.post('/graphql/', data=form_data, content_type=form_data.content_type)
    content = json.loads(response.content.decode('utf-8'))

    # Check for errors in the response
    assert 'errors' not in content, f"Errors in response: {content.get('errors')}"

    # Validate the response data
    assert 'data' in content, "Response data is missing"
    data = content['data']
    assert 'createOrUpdateArticle' in data, "Mutation result is missing"
    article_data = data['createOrUpdateArticle']

    # Ensure article data is present
    assert 'article' in article_data, "Article data is missing"
    article = article_data['article']

    # Validate article fields
    assert 'id' in article, "Article ID is missing"
    assert 'title' in article, "Article title is missing"
    assert 'content' in article, "Article content is missing"

    # Check specific values against expected data
    assert article['title'] == "New Article", "Incorrect article title"
    assert article['content'] == "Article content...", "Incorrect article content"
    assert article['id'] is not None, "Invalid article ID"
    assert article['thumbnail'] is not None, "Thumbnail URL is missing"

def test_comment_mutation(client_query):
    mutation = '''
        mutation CreateOrUpdateComment{
          createOrUpdateComment(articleId:1, email: "e2@e.com", text:"cmt-2", author: "author2"){
            comment{
              id
              commenter{
                id
                name
                email
              }
              article{
                id
                title
              }
              text
            }
          }
        }
    '''

    response = client_query(mutation, op_name='CreateOrUpdateComment')
    content = json.loads(response.content)
    assert 'errors' not in content

    # Additional assertions
    assert 'data' in content
    data = content['data']
    assert 'createOrUpdateComment' in data
    comment_data = data['createOrUpdateComment']
    assert 'comment' in comment_data
    comment = comment_data['comment']
    assert 'id' in comment
    assert 'commenter' in comment
    commenter = comment['commenter']
    assert 'id' in commenter
    assert 'name' in commenter
    assert 'email' in commenter
    assert commenter['name'] == "author2"
    assert commenter['email'] == "e2@e.com"
    assert 'article' in comment
    article = comment['article']
    assert 'id' in article
    assert 'title' in article
    assert article['id'] is not None
    # Add more assertions as needed based on expected behavior



# Add test functions for other mutations (e.g., CommenterMutation) similarly



def test_update_category_mutation(client_query):
    # Assume 'category_id' refers to an existing category to be updated
    category_id = 1  # Update with the ID of an existing category

    mutation = '''
        mutation CreateOrUpdateCategory($categoryId: ID!, $name: String!) {
          createOrUpdateCategory(id: $categoryId, name: $name) {
            category {
              id
              name
            }
          }
        }
    '''

    # Execute the update mutation
    response = client_query(mutation, op_name='CreateOrUpdateCategory', variables={'categoryId': category_id, 'name': 'Updated Category Name'})
    content = json.loads(response.content)

    # Check for errors in the response
    assert 'errors' not in content

    # Validate the updated category data
    assert 'data' in content
    data = content['data']
    assert 'createOrUpdateCategory' in data
    updated_category_data = data['createOrUpdateCategory']
    assert 'category' in updated_category_data
    updated_category = updated_category_data['category']

    # Ensure category data is updated correctly
    assert 'id' in updated_category
    assert 'name' in updated_category
    assert updated_category['id'] == str(category_id)
    assert updated_category['name'] == 'Updated Category Name'


# def test_update_article_mutation(client_query):
#     # Assume 'article_id' refers to an existing article to be updated
#     article_id = 1  # Update with the ID of an existing article
#
#     mutation = '''
#         mutation CreateOrUpdateArticle($articleId: ID!, $title: String!, $content: String!) {
#           createOrUpdateArticle(id: $articleId, title: $title, content: $content) {
#             article {
#               id
#               title
#               content
#             }
#           }
#         }
#     '''
#
#     # Execute the update mutation
#     response = client_query(mutation, op_name='CreateOrUpdateArticle', variables={'articleId': article_id, 'title': 'Updated Article Title', 'content': 'Updated Article Content'})
#     content = json.loads(response.content)
#
#     # Check for errors in the response
#     assert 'errors' not in content
#
#     # Validate the updated article data
#     assert 'data' in content
#     data = content['data']
#     assert 'createOrUpdateArticle' in data
#     updated_article_data = data['updateArticle']
#     assert 'article' in updated_article_data
#     updated_article = updated_article_data['article']
#
#     # Ensure article data is updated correctly
#     assert 'id' in updated_article
#     assert 'title' in updated_article
#     assert 'content' in updated_article
#     assert updated_article['id'] == str(article_id)
#     assert updated_article['title'] == 'Updated Article Title'
#     assert updated_article['content'] == 'Updated Article Content'


def test_update_comment_mutation(client_query):
    # Assume 'comment_id' refers to an existing comment to be updated
    comment_id = 43  # Update with the ID of an existing comment

    mutation = '''
        mutation CreateOrUpdateComment($commentId: ID!, $text: String!) {
          createOrUpdateComment(id: $commentId, text: $text) {
            comment {
              id
              text
            }
          }
        }
    '''

    # Execute the update mutation
    response = client_query(mutation, op_name='CreateOrUpdateComment', variables={'commentId': comment_id, 'text': 'Card available floor assume structure food system short. Trial full my agree need. - updated'})
    content = json.loads(response.content)

    # Check for errors in the response
    assert 'errors' not in content

    # Validate the updated comment data
    assert 'data' in content
    data = content['data']
    assert 'createOrUpdateComment' in data
    updated_comment_data = data['createOrUpdateComment']
    assert 'comment' in updated_comment_data
    updated_comment = updated_comment_data['comment']

    # Ensure comment data is updated correctly
    assert 'id' in updated_comment
    assert 'text' in updated_comment
    assert updated_comment['id'] == str(comment_id)
    assert updated_comment['text'] == 'Card available floor assume structure food system short. Trial full my agree need. - updated'



