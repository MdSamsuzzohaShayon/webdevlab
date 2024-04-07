import gql from 'graphql-tag';

const GET_ARTICLES = gql`
  query GetArticles {
    allArticles(limit: 10, start: 0) {
      title
      link
      id
      content
      category {
        id
        name
      }
      createdAt
      author {
        id
        name
      }
    }
    allAuthors {
      id
      name
      email
    }
    allCategories {
      id
      name
    }
  }
`;

const ADD_ARTICLE_RAW = `
mutation ($title: String!, $content: String!, $thumbnail: Upload!, $authorId: ID!, $categoryId: ID!, $id: ID) {
    createOrUpdateArticle(title: $title, content: $content, thumbnail: $thumbnail, authorId: $authorId, categoryId: $categoryId, id: $id) {
      article {
        id
        title
        content
        thumbnail
        author {
          id
          name
        }
        category {
          id
          name
        }
      }
    }
  }
`;

const GET_ARTICLE_BY_LINK = gql`
  query ArticleByLink($link: String) {
    articleByLink(link: $link) {
      content
      id
      link
      title
      thumbnail
      createdAt
      author {
        name
        id
      }
      category {
        id
        name
      }
    }
  }
`;

export { GET_ARTICLES, ADD_ARTICLE_RAW, GET_ARTICLE_BY_LINK };
