<template>
  <ClientOnly>
    <ArticleAdd :categories="data.allCategories" :authors="data.allAuthors" />
    <h1 class="mt-8">All articles</h1>
    <Article v-for="article in data.allArticles" :key="article.id" :article="article" />
  </ClientOnly>
</template>

<script setup lang="ts">
import { GET_ARTICLES } from '../../graphql/articles';
import type { IArticle, IAuthor, ICategory } from '~/types';

definePageMeta({
  layout: 'admin',
});

type Article = {
  allArticles: IArticle[];
  allAuthors: IAuthor[];
  allCategories: ICategory[];
};

const variables = { start: 0, limit: 20 };
const { data } = await useAsyncQuery<Article>(GET_ARTICLES, variables);
console.log({ data: data.value });
</script>
