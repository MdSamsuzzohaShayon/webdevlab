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

export { GET_ARTICLES };
