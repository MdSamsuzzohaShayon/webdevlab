<template>
  <section class="dark:bg-gray-800 dark:text-gray-100">
    <div class="container max-w-6xl p-6 mx-auto space-y-6 sm:space-y-12">
      <Article v-bind:first="true" v-bind:article="firstArticle" />
      <div class="grid justify-center grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <Article v-for="article in allArticles" :key="article.id" v-bind:first="false" v-bind:article="article" />

      </div>
      <div class="flex justify-center">
        <button type="button" class="px-6 py-3 text-sm rounded-md hover:underline dark:bg-gray-900 dark:text-gray-400">Load more posts...</button>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const props = defineProps(['allArticles', 'firstArticle']);
</script>
