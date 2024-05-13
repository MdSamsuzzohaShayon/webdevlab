<template>
  <div class="container">
    <section class="section section-1">
      <div class="row">
        <!-- Left side start  -->
        <div class="col-12 col-md-8">
          <div v-if="data?.allArticles && data?.allArticles.length > 0" class="card text-bg-dark">
            <CldImage
              :src="data?.allArticles[1].thumbnail"
              width="400"
              height="400"
              class="card-img"
              :alt="data?.allArticles[1].title"
            />
            <div class="card-img-overlay">
              <h5 class="card-title">{{ data?.allArticles[1].title }}</h5>
              <p class="card-text">
                {{ shortDesc(data?.allArticles[1].content, 200) }}
              </p>
              <p class="card-text">
                <small>{{
                  data?.allArticles[1].createdAt &&
                  formatReadableDate(data?.allArticles[1].createdAt)
                }}</small>
              </p>
            </div>
          </div>
        </div>
        <!-- Left side end  -->

        <!-- Right side start  -->
        <div class="col-12 col-md-4">
          <p class="blockquote-footer text-uppercase">This week's</p>
          <h2>Trending Posts</h2>

          <div v-if="data?.allArticles && data?.allArticles.length > 0" class="d-flex flex-column">
            <div
              v-for="article in data?.allArticles"
              :key="article.id"
              class="card mb-3"
              style="max-width: 540px"
            >
              <div class="row g-0">
                <div class="col-4">
                  <CldImage
                    :src="article.thumbnail"
                    width="400"
                    height="400"
                    class="img-fluid rounded-start"
                    :alt="article.title"
                  />
                </div>
                <div class="col-8">
                  <div class="card-body">
                    <h5 class="card-title">{{ article.title }}</h5>
                    <p class="card-text">{{ shortDesc(article.content, 200) }}</p>
                    <p class="card-text">
                      <small class="text-body-secondary">{{
                        article.createdAt && formatRelativeDate(article.createdAt)
                      }}</small>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Right side end  -->
      </div>
    </section>
  </div>
  <!-- <PostList
    v-if="data?.allArticles && data?.allArticles.length > 0"
    :all-articles="articles"
    :first-article="articles[0]"
  /> -->
</template>

<script lang="ts" setup>
import type { Ref } from 'vue';
import type { IArticle } from '../../types/Article';
import gql from 'graphql-tag';
// import { useQuery } from '@apollo/client';
// import { useQuery } from '@vue/apollo-composable';

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
      content
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
const { data, error } = await useAsyncQuery<ArticlesResult>(GET_ARTICLES, {start: 1, limit: 10});
console.log({ articles: data.value?.allArticles });

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
</script>
