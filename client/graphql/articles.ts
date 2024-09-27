import gql from 'graphql-tag';

const GET_ARTICLES = gql`
  query GetArticles($start: Int!, $limit: Int!) {
    allArticles(start: $start, limit: $limit) {
      id
      title
      thumbnail
      link
      content
      createdAt

      category {
        id
        name
      }

      author {
        id
        username
        firstName
        lastName
      }
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
          username
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
