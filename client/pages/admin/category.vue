<template>
  <ClientOnly>
    <h1>Category</h1>
    <!-- <Category v-for="cat in data.allCategories" :key="cat.id" :category="cat" /> -->
     <ul class="list-group">
      <li class="list-group-item" v-for="cat in state.allCategories" :key="cat.id">{{ cat.name }}</li>
     </ul>
    <CategoryAdd />
  </ClientOnly>
</template>

<script setup lang="ts">
import { GET_CATEGORIES } from '~/graphql/categories';
import type { ICategory } from '~/types';

definePageMeta({
  layout: 'admin',
});

interface IStateProps{
  allCategories: ICategory[];
}

const state = reactive<IStateProps>({allCategories: []});

type Category = {
  allCategories: ICategory[];
};

try {
  const { data } = await useAsyncQuery<Category>(GET_CATEGORIES);
  state.allCategories = data.value?.allCategories || [];
} catch (error) {
  console.log(error);

}
</script>
