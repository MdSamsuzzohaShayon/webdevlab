<template>
  <section class="dark:bg-gray-800 dark:text-gray-100">
    <div class="container mx-auto px-4">
      <Article v-bind:first="true" v-bind:article="firstArticle" />
      <!-- grid justify-between grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 content-between -->
      <div class="flex justify-between flex-wrap items-center gap-4">
        <Article v-for="article in allArticles" :key="article.id" v-bind:first="false" v-bind:article="article" />
      </div>
      <div class="flex justify-center mt-4">
        <button type="button"
          class="px-6 py-3 text-sm rounded-md hover:underline dark:bg-gray-900 dark:text-gray-400">Load more
          posts...</button>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const props = defineProps(['allArticles', 'firstArticle']);
</script>
