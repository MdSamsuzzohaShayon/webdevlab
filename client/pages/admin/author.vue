<template>
  <h1>Author</h1>
  <Author v-for="author in data.allAuthors" :key="author.id" :author="author" />
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'admin',
});

const query = gql`
  query GetAuthors {
    allAuthors {
      bio
      id
      name
      email
    }
  }
`;

interface IAuthor {
  id: number;
  name: string;
  bio: string;
  email: string;
}

type Author = {
  allAuthors: IAuthor[];
};
const { data } = await useAsyncQuery<Author>(query);
console.log(data.value);
</script>
