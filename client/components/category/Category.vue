<template>
  <h1>{{ category.name }}</h1>
</template>

<script setup lang="ts">
const props = defineProps(["category"]);
</script>
