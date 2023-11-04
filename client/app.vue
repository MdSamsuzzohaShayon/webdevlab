<!-- <NuxtWelcome /> -->
<template>
  <p>There are {{ JSON.stringify(data) || 0 }} ships.</p>
</template>

<script lang="ts" setup>
const query = gql`
  query GetArticles{
    allArticles{
      id
      title
      content
      createdAt
      author{
        id
        name
        email
      }
      category{
        id
        name
      }
    }
  }
`;
const variables = { limit: 5 };
const { data } = await useAsyncQuery(query);
console.log({data});

</script>
