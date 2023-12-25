<!-- <NuxtWelcome /> -->
<template>
    <div class="wrapper">
      <section class="px-5 py-10 dark:bg-gray-800 dark:text-gray-100">
        <div class="container grid grid-cols-12 mx-auto gap-y-6 md:gap-10">
          <Exclusive />
          <Showcase />
          <PopularLatest />
        </div>
      </section>
  
      <Posts v-bind:allArticles="data.allArticles" v-bind:firstArticle="data.allArticles[0]" />
    </div>
  </template>
  
  <script lang="ts" setup>
  import type { IArticle } from '../../types/Article';
  const query = gql`
    query GetArticles($limit: Int) {
      allArticles(limit: $limit) {
        id
        title
        content
        thumbnail
        link
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
  
  
  
  
  
  type ArticlesResult = {
    allArticles: IArticle[]
  }
  
  
  const variables = { limit: 20 };
  const { data } = await useAsyncQuery<ArticlesResult>(query, variables);
  // console.log({ allArticles: data.value.allArticles });
  </script>
  