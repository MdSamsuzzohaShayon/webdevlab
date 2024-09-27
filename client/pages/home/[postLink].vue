<template>
  <ClientOnly fallback-tag="span" fallback="Loading...">
    <ArticleExpand :post-link="$route.params.postLink" />
  </ClientOnly>
</template>
