<!-- <NuxtWelcome /> -->
<template>
    <p>There are {{ JSON.stringify(data) || 0 }} ships.</p>
  </template>
  
  <script lang="ts" setup>
  const query = gql`
    query GetArticles($limit: Int) {
      allArticles(limit: $limit) {
        id
        title
        content
        createdAt
        author {
          id
          name
          email
        }
        category {
          id
          name
        }
      }
    }
  `;
  const variables = { limit: 20 };
  const { data } = await useAsyncQuery(query, variables );
  console.log({ data });
  </script>
  