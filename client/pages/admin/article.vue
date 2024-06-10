<template>
  <div class="container">
    <ArticleAdd v-if="state.allCategories.length > 0" :categories="state.allCategories" />
    <h1 class="mt-8">All articles</h1>
    <!-- <Article  v-for="article in data.allArticles" :key="article.id" :article="article" /> -->
  </div>
</template>

<script setup lang="ts">
import { GET_CATEGORIES } from '~/graphql/categories';
import { GET_ARTICLES } from '../../graphql/articles';
import type { IArticle, IAuthor, ICategory } from '~/types';

definePageMeta({
  layout: 'admin',
});

type Category = {
  allCategories: ICategory[];
};


interface IStateProps{
  allCategories: ICategory[];
}

const state = reactive<IStateProps>({allCategories: []});


try {
  const { data } = await useAsyncQuery<Category>(GET_CATEGORIES);
  console.log({ data: data.value?.allCategories });
  state.allCategories = data.value?.allCategories || [];
} catch (error) {
  console.log(error);
  
}
</script>
