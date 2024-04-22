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
      v-if="data?.allArticles && data?.allArticles.length > 0"
      :all-articles="articles"
      :first-article="articles[0]"
    />
  </div>
</template>

<script lang="ts" setup>
import type { Ref } from 'vue';
import type { IArticle } from '../../types/Article';

type ArticlesResult = {
  allArticles: IArticle[];
};

const GET_ARTICLES = gql`
  query GetArticles($start: Int!, $limit: Int!) {
    allArticles(start: $start, limit: $limit) {
      id
      title
      thumbnail
      link
      createdAt

      category {
        id
        name
      }

      author {
        id
        username
        firstName
        lastName
      }
    }
  }
`;

// Fetch articles
const { data, error, loading } = await useAsyncQuery<ArticlesResult>(GET_ARTICLES, {
  limit: 20,
  start: 0,
});
console.log({articles: data?.value?.allArticles});

// Log data in a nice-looking format
const articles: Ref<IArticle[]> = ref([]);
if (data) {
  articles.value = data?.value?.allArticles ? data?.value?.allArticles : [];
  console.log('Fetched articles:', articles);
}



// Handle error
if (error) {
  console.error('Error fetching articles:', error);
}

// Show loading indicator if data is still being fetched
if (loading) {
  console.log('Fetching articles...');
}
</script>
