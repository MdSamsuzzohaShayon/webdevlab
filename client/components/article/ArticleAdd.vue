<template>
  <ClientOnly>
    <h1>Add Article</h1>
    <form class="mb-4" v-on:submit.prevent="handleArticleAdd">
      <div class="input-group mb-3">
        <label for="title">Title</label>
        <input type="text" class="border outline-none bg-gray-300" name="title" id="title" v-model="articleState.title" />
      </div>
      <div class="input-group flex mb-3 flex-col items-start gap-2">
        <label for="thumbnail">Thumbnail</label>
        <input type="file" class="border outline-none bg-gray-300" name="thumbnail" id="thumbnail"
          v-on:change="handleFileChange" />
        <img v-if="imgUrl" v-bind:src="imgUrl" class="w-full h-36 object-cover object-center" />
      </div>
      <div class="input-group mb-3">
        <label for="content">Content</label>
        <QuillEditor v-model:content="state.content" :options="options" toolbar="essential" theme="snow" @editorChange="handleContentChange"
          contentType="html" />
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
        <select name="category" id="category" v-model="articleState.category">
          <option v-for="cat in props.categories" v-bind:value="cat.id">{{ cat.name }}</option>
        </select>
      </div>
      <div class="input-group mb-3">
        <label for="author">Author</label>
        <select name="author" id="author" v-model="articleState.author">
          <option v-for="a in props.authors" v-bind:value="a.id">{{ a.name }}</option>
        </select>
      </div>
      <div class="input-group mb-3">
        <label for="link">Link</label>
        <input type="text" class="border outline-none bg-gray-300" name="link" id="link" v-model="articleState.link" />
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
import { ADD_ARTICLE_RAW } from '../../graphql/articles';

const isReadOnly = false;

const articleState = reactive({
  title: '',
  category: '',
  author: '',
  link: '',
});

const uploadedImg = ref<File | null>(null);
const imgUrl = ref<string | null>(null);

const options = {
  debug: "info",
  // modules: {
  //   toolbar:  "essential" /*["bold", "italic", "underline"]*/,
  // },
  placeholder: "Compose an epic...",
  readOnly: isReadOnly,
  theme: "snow",
};

const initialContent = `
  <h1>Main Title</h1>
  <h2>Subheading 1</h2>
  <p>Content...</p>
  <h2>Subheading 2</h2>
  <p>Content...</p>
`;


const state = reactive({ content: initialContent });
const props = defineProps(["categories", "authors"]);

const handleArticleAdd = async (e: Event) => {
  e.preventDefault();
  // const formData = {
  //   title: articleState.title,
  //   content: state.content,
  //   category: articleState.category,
  //   author: articleState.author,
  //   link: articleState.link,
  // };
  const formData = new FormData();


  const myHeaders = new Headers();
  myHeaders.append("Cookie", "csrftoken=ccS5qh2RZofjzKhe6KeN51RMYOGQAb5t");

  const newImgFile = uploadedImg.value as File;

  const operations = {
    query: ADD_ARTICLE_RAW,
    variables: {
      title: articleState.title,
      content: state.content,
      thumbnail: null, // You may need to handle thumbnail separately based on your requirements
      authorId: articleState.author,
      categoryId: articleState.category,
    },
  };

  formData.set("operations", JSON.stringify(operations));
  formData.set("map", "{\n  \"0\": [\"variables.thumbnail\"]\n}");
  formData.set("0", newImgFile);

  const response = await fetch("http://localhost:8000/graphql/", {
    method: 'POST',
    headers: myHeaders,
    body: formData,
    redirect: 'follow'
  });

  console.log(response);
  
};

const handleFileChange = (e: Event) => {
  e.preventDefault();
  const inputEl = e.target as HTMLInputElement;
  if (inputEl.files && inputEl.files.length > 0) {
    uploadedImg.value = inputEl.files[0];
    const objectUrl = URL.createObjectURL(inputEl.files[0]);
    imgUrl.value = objectUrl;;
  }
}

const handleContentChange = (e: Delta) => {
  // console.log(e);
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
