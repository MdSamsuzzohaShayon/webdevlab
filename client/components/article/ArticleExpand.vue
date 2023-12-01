<template>
  <main className="continer mx-auto px-4">
    <div class="relative w-full h-80">
      <div class="static h-full">
        <img
          src="https://images.unsplash.com/photo-1493770348161-369560ae357d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80"
          alt="thumbnail"
          class="w-full h-full object-cover object-center"
        />
      </div>
      <div class="absolute bottom-2 left-2">
        <h1 className="text-4xl font-semibold text-gray-100 leading-tight">
          {{ data.articleByLink.title }}
        </h1>
        <img class="img-wrapper w-12 h-12 rounded-full border-4 border-gray-200" src="https://randomuser.me/api/portraits/men/97.jpg" alt="author" />
        <p className="font-semibold text-gray-200 text-sm">{{ data.articleByLink.author.name }}</p>
        <p className="font-semibold text-gray-400 text-xs">{{ data.articleByLink.createdAt }}</p>
      </div>
    </div>
    <!-- <QuillEditor v-model="initialContent" :options="options" /> -->
    <p>{{ data.articleByLink.content }}</p>
  </main>
</template>

<script lang="ts" setup>
// @ts-ignore
import {Delta} from '@vueup/vue-quill';
import type { IArticle } from "../../types/Article";

const props = defineProps(["postLink"]);

const query = gql`
  query ArticleByLink($link: String) {
    articleByLink(link: $link) {
      content
      createdAt
      id
      link
      title
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

const isReadOnly = true;

const options = {
  debug: "info",
  modules: {
    toolbar: isReadOnly ? false : ["bold", "italic", "underline"],
  },
  placeholder: "Compose an epic...",
  readOnly: true,
  theme: "snow",
};

const initialContent = new Delta([
  {
    insert: "sdsdssdds\n\nhhg\nhello\n\n\nho\n\ngoal",
  },
  {
    attributes: {
      list: "ordered",
    },
    insert: "\n",
  },
  {
    insert: "sure",
  },
  {
    attributes: {
      list: "ordered",
    },
    insert: "\n",
  },
  {
    insert: "be",
  },
  {
    attributes: {
      list: "ordered",
    },
    insert: "\n",
  },
  {
    insert: "wit",
  },
  {
    insert: "\n",
    attributes: {
      list: "ordered",
    },
  },
]);

type ArticlesResult = {
  articleByLink: IArticle;
};

const variables = { link: props.postLink };
const { data } = await useAsyncQuery<ArticlesResult>(query, variables);
console.log(data);
</script>
