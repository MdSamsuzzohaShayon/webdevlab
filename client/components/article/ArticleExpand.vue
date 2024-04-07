<template>
  <main className="continer mx-auto px-4">
    <div v-if="data?.articleByLink" class="relative w-full h-80">
      <div class="static h-full">
        <CldImage
          v-if="
            data?.articleByLink &&
            data.articleByLink.thumbnail &&
            data.articleByLink.thumbnail !== ''
          "
          :src="data.articleByLink.thumbnail"
          width="400"
          height="400"
          class="w-full h-full object-cover object-center"
          :alt="data.articleByLink.title"
        />
        <img
          v-else
          src="https://images.unsplash.com/photo-1493770348161-369560ae357d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80"
          alt="thumbnail"
          class="w-full h-full object-cover object-center"
        />
      </div>
      <div class="absolute bottom-2 left-2">
        <h1 className="text-4xl font-semibold text-gray-100 leading-tight">
          {{ data.articleByLink.title }}
        </h1>
        <img
          class="img-wrapper w-12 h-12 rounded-full border-4 border-gray-200"
          src="https://randomuser.me/api/portraits/men/97.jpg"
          alt="author"
        />
        <p className="font-semibold text-gray-200 text-sm">{{ data.articleByLink.author.name }}</p>
        <p className="font-semibold text-gray-400 text-xs">{{ data.articleByLink?.createdAt }}</p>
      </div>
      <div v-html="data.articleByLink.content"></div>
    </div>
    <div v-else class="no-article-found">
      <p class="text-text-red-700">No article found!</p>
    </div>
    <!-- <QuillEditor v-model="state.content" theme="snow" :options="options" /> -->
  </main>
</template>

<script lang="ts" setup>
// @ts-ignore
// eslint-disable-next-line @typescript-eslint/no-unused-vars
import { Delta, QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import type { IArticle } from '../../types/Article';
import { GET_ARTICLE_BY_LINK } from '~/graphql/articles';

const props = defineProps(['postLink']);

type ArticlesResult = {
  articleByLink: IArticle;
};

const variables = { link: props.postLink };
const { data } = await useAsyncQuery<ArticlesResult>(GET_ARTICLE_BY_LINK, variables);
console.log({ ...data });
</script>
