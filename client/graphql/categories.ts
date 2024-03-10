import gql from "graphql-tag";

const CREATE_CATEGORY = gql`
mutation CreateCategory($name:String!){
    createOrUpdateCategory(name:$name){
      category{
        id
        name
      }
    }
  }
`;

export {CREATE_CATEGORY};