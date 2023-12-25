<template>
  <ClientOnly>
    <ArticleAdd v-bind:categories="data.allCategories" v-bind:authors="data.allAuthors" />
    <h1 class="mt-8">All articles</h1>
    <Article v-for="article in data.allArticles" v-bind:key="article.id" v-bind:article="article" />
  </ClientOnly>
</template>

<script setup lang="ts">
import type { IArticle, IAuthor, ICategory } from "~/types";
import { GET_ARTICLES } from "../../graphql/articles";

definePageMeta({
  layout: "admin",
});

type Article = {
  allArticles: IArticle[];
  allAuthors: IAuthor[];
  allCategories: ICategory[];
};

const variables = { start: 0, limit: 20 };
const { data } = await useAsyncQuery<Article>(GET_ARTICLES, variables);
console.log(data.value);
</script>
