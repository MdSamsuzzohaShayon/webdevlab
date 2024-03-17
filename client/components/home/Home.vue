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
  
      <Posts v-if="data.allArticles && data.allArticles.length > 0" v-bind:allArticles="data.allArticles" v-bind:firstArticle="data.allArticles[0]" />
    </div>
  </template>
  
  <script lang="ts" setup>
  import { GET_ARTICLES } from '~/graphql/articles';
import type { IArticle } from '../../types/Article';
  
  
  
  
  
  type ArticlesResult = {
    allArticles: IArticle[]
  }
  
  
  const variables = { limit: 20 };
  const { data } = await useAsyncQuery<ArticlesResult>(GET_ARTICLES, variables);
  console.log({ allArticles: data.value.allArticles });
  </script>
  