// uri: 'http://localhost:8000/graphql/', // Set your GraphQL API endpoint
import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client/core';

export default defineNuxtPlugin({
  name: 'apollo-client',
  setup() {
    // HTTP connection to the API
    const httpLink = createHttpLink({
      // You should use an absolute URL here
      uri: 'http://localhost:8000/graphql/',
    })

    // Cache implementation
    const cache = new InMemoryCache()

    // Create the apollo client
    const apolloClient = new ApolloClient({
      link: httpLink,
      cache,
    })

    // Provide the Apollo client to the Nuxt app
    return {
      provide: {
        $apollo: apolloClient,
        $value: 123
      },
    };
  },
});





