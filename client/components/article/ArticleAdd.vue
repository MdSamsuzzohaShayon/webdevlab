<template>
  <ClientOnly>
    <h1>Add Article</h1>
    <form class="mb-4" v-on:submit.prevent="handleArticleAdd">
      <div class="input-group mb-3">
        <label for="title">Title</label>
        <input type="text" class="border outline-none bg-gray-300" name="title" id="title" />
      </div>
      <div class="input-group mb-3">
        <label for="content">Content</label>
        <QuillEditor v-model:content="state.content" theme="snow" v-bind:options="options" v-on:editorChange="handleContentChange" contentType="delta" />
        <!-- <div class="border border-green-500">
          <h2>Display content</h2>
          <QuillEditor v-model="initialContent" :options="options" />
        </div> -->
      </div>
      <div class="input-group mb-3">
        <label for="createdAt">Date</label>
        <input type="datetime-local" name="createdAt" id="createdAt" />
      </div>
      <div class="input-group mb-3">
        <label for="category">Category</label>
        <select name="category" id="category">
          <option v-for="cat in props.categories" v-bind:value="cat.id">{{ cat.name }}</option>
        </select>
      </div>
      <div class="input-group mb-3">
        <label for="author">Author</label>
        <select name="author" id="author">
          <option v-for="a in props.authors" v-bind:value="a.id">{{ a.name }}</option>
        </select>
      </div>
      <div class="input-group mb-3">
        <label for="link">Link</label>
        <input type="text" class="border outline-none bg-gray-300" name="link" id="link" />
      </div>
      <div class="input-group">
        <button type="submit">Add</button>
      </div>
    </form>
  </ClientOnly>
</template>

<script setup lang="ts">
// @ts-ignore
import { QuillEditor, Delta, Quill } from "@vueup/vue-quill";
import "@vueup/vue-quill/dist/vue-quill.snow.css";

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


const state = reactive({ content: initialContent });
const props = defineProps(["categories", "authors"]);

const handleArticleAdd = (e) => {
  console.log({ state: state.content });
};

const handleContentChange = (e: EventListener) => {
  console.log(e);
};
</script>

<style scoped lang="css">
:deep(.ql-editor) {
  min-height: 200px;
}
:deep(.ql-toolbar.ql-snow) {
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
}
:deep(.ql-container.ql-snow) {
  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
}
</style>
