<template>
  <main className="continer mx-auto px-4">
    <div class="relative w-full h-80" v-if="data?.articleByLink">
      <div class="static h-full">
        <CldImage v-if="data?.articleByLink && data.articleByLink.thumbnail && data.articleByLink.thumbnail !== ''"
          v-bind:src="data.articleByLink.thumbnail" width="400" height="400"
          class="w-full h-full object-cover object-center" v-bind:alt="data.articleByLink.title" />
        <img v-else
          src="https://images.unsplash.com/photo-1493770348161-369560ae357d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80"
          alt="thumbnail" class="w-full h-full object-cover object-center" />
      </div>
      <div class="absolute bottom-2 left-2">
        <h1 className="text-4xl font-semibold text-gray-100 leading-tight">
          {{ data.articleByLink.title }}
        </h1>
        <img class="img-wrapper w-12 h-12 rounded-full border-4 border-gray-200"
          src="https://randomuser.me/api/portraits/men/97.jpg" alt="author" />
        <p className="font-semibold text-gray-200 text-sm">{{ data.articleByLink.author.name }}</p>
        <p className="font-semibold text-gray-400 text-xs">{{ data.articleByLink?.createdAt }}</p>
      </div>
      <div v-html="data.articleByLink.content"></div>
    </div>
    <div class="no-article-found" v-else>
      <p class="text-text-red-700">No article found!</p>
    </div>
    <!-- <QuillEditor v-model="state.content" theme="snow" :options="options" /> -->
  </main>
</template>

<script lang="ts" setup>
// @ts-ignore
import { Delta, QuillEditor } from '@vueup/vue-quill';
import "@vueup/vue-quill/dist/vue-quill.snow.css";
import type { IArticle } from "../../types/Article";

const props = defineProps(["postLink"]);

const query = gql`
  query ArticleByLink($link: String) {
    articleByLink(link: $link) {
      content
      id
      link
      title
      thumbnail
      createdAt
      author {
        name
        id
      }
      category {
        id
        name
      }
    }
  }
`;

type ArticlesResult = {
  articleByLink: IArticle;
};

const variables = { link: props.postLink };
const { data } = await useAsyncQuery<ArticlesResult>(query, variables);
console.log({ ...data });
</script>
