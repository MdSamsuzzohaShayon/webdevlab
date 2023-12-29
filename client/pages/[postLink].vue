<template>
  <ClientOnly fallback-tag="span" fallback="Loading...">
    <ArticleExpand v-bind:postLink="$route.params.postLink" />
  </ClientOnly>
</template>