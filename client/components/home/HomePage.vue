<template>
  <div class="container">
    <section class="section section-1">
      <div class="row">
        <!-- Left side / Top side on mobile start  -->
        <div class="col-12 col-md-8">
          <div v-if="data?.allArticles && data?.allArticles.length > 0" class="card text-bg-dark" id="feature-card">
            <CldImage :src="data?.allArticles[1].thumbnail" width="800" height="800" class="card-img"
              :alt="data?.allArticles[1].title" />
            <div class="card-img-overlay d-flex flex-column justify-content-end">
              <h1 class="card-title">{{ data?.allArticles[1].title }}</h1>
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
        <!-- Left side / Top side on mobile end  -->

        <!-- Right side / bottom side on the mobile start  -->
        <div class="col-12 col-md-4">
          <p class="text-uppercase">This week's</p>
          <h2>Trending Posts</h2>

          <div v-if="data?.allArticles && data?.allArticles.length > 0" class="d-flex flex-column" id="latest-posts">
            <div v-for="article in data?.allArticles.slice(0, 4)" :key="article.id"
              class="card mb-3 latest-post-card border border-bottom" style="max-width: 540px">
              <div class="row">
                <div class="col-4">
                  <CldImage :src="article.thumbnail" width="400" height="400" class="img-fluid rounded-start"
                    :alt="article.title" />
                </div>
                <div class="col-8">
                  <div class="card-body">
                    <h2 class="card-title">{{ article.title }}</h2>
                    <!-- <p class="card-text">{{ shortDesc(article.content, 200) }}</p>
                    <p class="card-text">
                      <small class="text-body-secondary">{{
                        article.createdAt && formatRelativeDate(article.createdAt)
                      }}</small>
                    </p> -->
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Right side / bottom side on the mobile end  -->
      </div>
    </section>

    <section class="section section-2">
      <div class="row">
        <p class="text-uppercase">Popular</p>
        <h2>Tech News</h2>
      </div>
    </section>
  </div>
</template>

<script lang="ts" setup>
import type { Ref } from 'vue';
import type { IArticle } from '../../types/Article';
import { GET_ARTICLES } from '~/graphql/articles';
// import { useQuery } from '@apollo/client';
// import { useQuery } from '@vue/apollo-composable';

const state = reactive({
  allArticles: [],
  latestArticles: [],
  newsArticles: [],
  tutorialArticles: [],
  trendingArticles: [],
});

type ArticlesResult = {
  allArticles: IArticle[];
};



// Fetch articles
const { data, error } = await useAsyncQuery<ArticlesResult>(GET_ARTICLES, { start: 1, limit: 10 });
console.log({ articles: data.value?.allArticles });

// Log data in a nice-looking format
const articles: Ref<IArticle[]> = ref([]);
if (data) {
  articles.value = data?.value?.allArticles ? data?.value?.allArticles : [];

  // Seperate all category
  // for (let i = 0; i < array.length; i++) {
  //   const element = array[i];
  //   console.log('Fetched articles:', articles);
  // }
}

// Handle error
if (error) {
  console.error('Error fetching articles:', error);
}
</script>
