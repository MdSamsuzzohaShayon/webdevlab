<template>
  <h1>{{ author.name }}</h1>
  <p class="border-b">{{ author.bio }}</p>
</template>

<script setup lang="ts">
// eslint-disable-next-line @typescript-eslint/no-unused-vars
const props = defineProps(['author']);
</script>
