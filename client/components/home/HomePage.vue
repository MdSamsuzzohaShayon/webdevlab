<template>
  <div class="container">
    <section class="section section-1">
      <div class="row">
        <!-- Left side / Top side on mobile start  -->
        <div class="col-12 col-md-8">
          <NuxtLink v-if="state.latestArticles && state.latestArticles.length > 0" class="card text-bg-dark text-decoration-none" id="feature-card" :to="state.latestArticles[0].link">
            <CldImage :src="state.latestArticles[1].thumbnail" width="800" height="800" class="card-img"
              :alt="state.latestArticles[1].title" />
            <div class="card-img-overlay d-flex flex-column justify-content-end">
              <h1 class="card-title">{{ state.latestArticles[1].title }}</h1>
              <p class="card-text">
                {{ shortDesc(state.latestArticles[1].content, 200) }}
              </p>
              <p class="card-text">
                <small>{{
            state.latestArticles[1].createdAt &&
            formatReadableDate(state.latestArticles[1].createdAt)
          }}</small>
              </p>
            </div>
          </NuxtLink>
        </div>
        <!-- Left side / Top side on mobile end  -->

        <!-- Right side / bottom side on the mobile start  -->
        <div class="col-12 col-md-4">
          <p class="text-uppercase">This week's</p>
          <h2>Trending Posts</h2>

          <div v-if="state.trendingArticles && state.trendingArticles.length > 0" class="d-flex flex-column"
            id="latest-posts">
            <NuxtLink v-for="trendingArticle in state.trendingArticles.slice(0, 4)" :key="trendingArticle.id"
              class="card mb-3 latest-post-card border border-bottom text-decoration-none" :to="trendingArticle.link" style="max-width: 540px">
              <div class="row">
                <div class="col-4">
                  <CldImage :src="trendingArticle.thumbnail" width="400" height="400" class="img-fluid rounded-start"
                    :alt="trendingArticle.title" />
                </div>
                <div class="col-8">
                  <div class="card-body">
                    <h2 class="card-title">{{ trendingArticle.title }}</h2>
                    <!-- <p class="card-text">{{ shortDesc(article.content, 200) }}</p>
                    <p class="card-text">
                      <small class="text-body-secondary">{{
                        article.createdAt && formatRelativeDate(article.createdAt)
                      }}</small>
                    </p> -->
                  </div>
                </div>
              </div>
            </NuxtLink>
          </div>
        </div>
        <!-- Right side / bottom side on the mobile end  -->
      </div>
    </section>

    <section class="section section-2">
      <div class="row">
        <p class="text-uppercase">Popular</p>
        <h2>Tutorial</h2>
      </div>
      <div class="row">
        <NuxtLink class="col-md-4 text-decoration-none" v-if="state.tutorialArticles && state.tutorialArticles.length > 0"
              v-for="tutorialArticle in state.tutorialArticles.slice(1, 5)" :key="tutorialArticle.id" v-bind:to="tutorialArticle.link" >
          <div class="card mb-3" style="width: 100%;"  >
            <div class="row g-0">
              <div class="col-md-4">
                <CldImage :src="tutorialArticle.thumbnail" width="800" height="800" class="card-img img-fluid rounded-start"
                  :alt="tutorialArticle.title" />
              </div>
              <div class="col-md-8">
                <div class="card-body">
                  <h5 class="card-title">{{ tutorialArticle.title }}</h5>
                  <p class="card-text">{{ shortDesc(tutorialArticle.content, 200) }}</p>
                  <p class="card-text"><small class="text-body-secondary">{{
            tutorialArticle.createdAt &&
            formatReadableDate(tutorialArticle.createdAt)
                      }}</small></p>
                </div>
              </div>
            </div>
          </div>
        </NuxtLink>
      </div>
    </section>

    <section class="section section-3">
      <div class="row">
        <p class="text-uppercase">Popular</p>
        <h2>Tech News</h2>
      </div>
      <div class="row">
        <div class="col-md-5">
          <div v-if="state.newsArticles && state.newsArticles.length > 0" class="card text-bg-dark">
            <CldImage :src="state.newsArticles[1].thumbnail" width="800" height="800" class="card-img"
              :alt="state.newsArticles[1].title" />
            <div class="card-img-overlay d-flex flex-column justify-content-end">
              <h1 class="card-title">{{ state.newsArticles[1].title }}</h1>
              <p class="card-text">
                {{ shortDesc(state.newsArticles[1].content, 200) }}
              </p>
              <p class="card-text">
                <small>{{
            state.newsArticles[1].createdAt &&
            formatReadableDate(state.newsArticles[1].createdAt)
          }}</small>
              </p>
            </div>
          </div>
        </div>
        <div class="col-md-7">
          <div class="row">
            <NuxtLink v-if="state.newsArticles && state.newsArticles.length > 0"
              v-for="newsArticle in state.newsArticles.slice(1, 5)" :to="newsArticle.link" :key="newsArticle.id" class="col-md-6 text-decoration-none">
              <div class="card text-bg-dark">
                <CldImage :src="newsArticle.thumbnail" width="800" height="800" class="card-img"
                  :alt="newsArticle.title" />
                <div class="card-img-overlay d-flex flex-column justify-content-end">
                  <h1 class="card-title">{{ newsArticle.title }}</h1>
                  <p class="card-text">
                    {{ shortDesc(newsArticle.content, 200) }}
                  </p>
                  <p class="card-text">
                    <small>{{
            newsArticle.createdAt &&
            formatReadableDate(newsArticle.createdAt)
                      }}</small>
                  </p>
                </div>
              </div>
            </NuxtLink>
            <div class="col-md-6">
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts" setup>
import type { Ref } from 'vue';
import type { IArticle } from '../../types/Article';
import { GET_ARTICLES } from '~/graphql/articles';

interface IStateProps {
  allArticles: IArticle[];
  latestArticles: IArticle[];
  newsArticles: IArticle[];
  tutorialArticles: IArticle[];
  trendingArticles: IArticle[];
}

const state = reactive<IStateProps>({
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
const { data, error } = await useAsyncQuery<ArticlesResult>(GET_ARTICLES, { start: 1, limit: 50 });
// console.log({ articles: data.value?.allArticles });

// Log data in a nice-looking format
// const articles: Ref<IArticle[]> = ref([]);
if (data) {
  const allArticles: IArticle[] = data?.value?.allArticles ? data?.value?.allArticles : [];
  state.allArticles = allArticles;

  const latestArticles = [], newsArticles = [], tutorialArticles = [], trendingArticles = [];
  // Seperate all category
  for (let i = 0; i < allArticles.length; i += 1) {
    const element = allArticles[i];
    if (element.category.name.toUpperCase() === "LATEST") {
      latestArticles.push(element);
    } else if (element.category.name.toUpperCase() === "NEWS") {
      newsArticles.push(element);
    } else if (element.category.name.toUpperCase() === "TUTORIAL") {
      tutorialArticles.push(element);
    } else if (element.category.name.toUpperCase() === "TRENDING") {
      trendingArticles.push(element);
    }
  }

  state.latestArticles = latestArticles;
  state.newsArticles = newsArticles;
  state.tutorialArticles = tutorialArticles;
  state.trendingArticles = trendingArticles;
}

// Handle error
if (error) {
  console.error('Error fetching articles:', error);
}
</script>
