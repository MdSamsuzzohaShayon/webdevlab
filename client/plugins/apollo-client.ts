// uri: 'http://localhost:8000/graphql/', // Set your GraphQL API endpoint
import { ApolloClient } from 'apollo-client';
import { HttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';

export default defineNuxtPlugin({
  name: 'apollo-client',
  setup() {
    const apolloClient = new ApolloClient({
      link: new HttpLink({
        uri: 'http://localhost:8000/graphql/', // Set your GraphQL API endpoint
        credentials: 'same-origin', // Additional configurations if needed
      }),
      cache: new InMemoryCache(),
    });

    // Provide the Apollo client to the Nuxt app
    return {
      provide: {
        $apollo: apolloClient,
      },
    };
  },
});