import gql from 'graphql-tag';

const GET_CATEGORIES = gql`
query GetCategories{
  allCategories{
    id
    name
  }
}
`;

const GET_CATEGORY_WITH_ARTICLES = gql`
query GetCategory($id: Int){
  categoryById(id:$id){
    id
    name
    articleSet{
      id
      title
      content
      thumbnail
      createdAt
      author{
        id
        email
        firstName
        lastName
      }
      link
    }
  }
}
`;

const CREATE_CATEGORY = gql`
  mutation CreateCategory($name: String!) {
    createOrUpdateCategory(name: $name) {
      category {
        id
        name
      }
    }
  }
`;

export { CREATE_CATEGORY, GET_CATEGORIES, GET_CATEGORY_WITH_ARTICLES };
