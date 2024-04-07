<template>
  <div class="wrapper">
    <section class="px-5 py-10 dark:bg-gray-800 dark:text-gray-100">
      <div class="container grid grid-cols-12 mx-auto gap-y-6 md:gap-10">
        <ExclusiveArticles />
        <ShowcaseContent />
        <PopularLatest />
      </div>
    </section>

    <PostList
      v-if="data.allArticles && data.allArticles.length > 0"
      :all-articles="data.allArticles"
      :first-article="data.allArticles[0]"
    />
  </div>
</template>

<script lang="ts" setup>
import type { IArticle } from '../../types/Article';
import { GET_ARTICLES } from '~/graphql/articles';

type ArticlesResult = {
  allArticles: IArticle[];
};

const variables = { limit: 20 };
const { data } = await useAsyncQuery<ArticlesResult>(GET_ARTICLES, variables);
</script>
