<template>
  <!-- <NuxtLink to="/posts/postid">
    <div
      v-bind:class="{`max-w-sm mx-auto group hover:no-underline focus:no-underline dark:bg-gray-900 ${props.first ? 'block gap-3 sm:max-w-full lg:grid lg:grid-cols-12' : ''}`}"
    >
      <img
        role="presentation"
        src="https://source.unsplash.com/random/480x360"
        alt=""
        class="object-cover w-full h-64 rounded sm:h-96 lg:col-span-7 dark:bg-gray-500"
      />
      <div class="p-6 space-y-2 lg:col-span-5">
        <h3 class="text-2xl font-semibold sm:text-4xl group-hover:underline group-focus:underline">Noster tincidunt reprimique ad pro</h3>
        <span class="text-xs dark:text-gray-400">February 19, 2021</span>
        <p>Ei delenit sensibus liberavisse pri. Quod suscipit no nam. Est in graece fuisset, eos affert putent doctus id.</p>
      </div>
    </div>
  </NuxtLink> -->
  <NuxtLink rel="noopener noreferrer" v-bind:to="'http://localhost:3000/' + article.link"
    class="max-w-sm mx-auto group hover:no-underline focus:no-underline dark:bg-gray-900">
    <CldImage v-if="article.thumbnail && article.thumbnail !== ''" v-bind:src="article.thumbnail" width="400" height="400" class="object-cover w-full rounded h-44 dark:bg-gray-500"
      v-bind:alt="article.title" />
    <img v-else class="object-cover w-full rounded h-44 dark:bg-gray-500"
      src="https://source.unsplash.com/random/480x360?1" />
    <div class="p-6 space-y-2">
      <h3 class="text-2xl font-semibold group-hover:underline group-focus:underline">{{ article.title }}</h3>
      <span class="text-xs dark:text-gray-400">{{ article.createdAt }}</span>
      <p>
        {{ article.content }}
      </p>
    </div>
  </NuxtLink>
</template>

<script setup lang="ts">
// import { IArticleProps } from "../../types";
const props = defineProps(["first", "article"]);
// console.log(props.article);
// {FRONTEND_URL} + 

</script>
