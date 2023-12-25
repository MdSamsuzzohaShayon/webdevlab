### Queries
  
  - Get Article By Slug
  ```
    query GetPostBySlug($slug: String){
    articleByLink(link: $slug){
        id
        title
        thumbnail
    }
    }
  ```

  - Get all articles
  ```
    query GetAllArticle{
        allArticles{
            id
            title
            content
            thumbnail
            link
            createdAt
            author{
                id
                name
            }
            category{
                id
            }
        }
    }
  ```

### Mutations
  - Create category
  ```
    mutation CreateCategory{
    createOrUpdateCategory(name: "Category - 10" ){
        category{
        id
        name
        }
    }
    }
  ```

  - Create an article with curl 
  ```
    curl --location 'http://localhost:8000/graphql/' \
    --form 'operations="{
    \"query\": \"mutation ($title: String!, $content: String!, $thumbnail: Upload!, $authorId: ID!, $categoryId: ID!, $id: ID) { createOrUpdateArticle(title: $title, content: $content, thumbnail: $thumbnail, authorId: $authorId, categoryId: $categoryId, id: $id) { article { id title content thumbnail author { id name } category { id name } } } }\",
    \"variables\": {
        \"title\": \"Test Article - 10\",
        \"content\": \"This is a test article\",
        \"thumbnail\": null,
        \"authorId\": \"1\",
        \"categoryId\": \"1\"
    }
    }"' \
    --form 'map="{
    \"0\": [\"variables.thumbnail\"]
    }"' \
    --form '0=@"/home/shayon/Pictures/pexels-daniel-reis-19575513.jpg"'
  ```

  - Create a comment
  ```
    mutation CreateComment{
        createOrUpdateComment(author: "Md SHayon", email:"eg1@e.com", text: "This is comment 1", articleId: 8){
            comment{
                id
                article{
                    id
                    title
                    link
                }
                author
                email
                text
            }
        }
    }
  ```