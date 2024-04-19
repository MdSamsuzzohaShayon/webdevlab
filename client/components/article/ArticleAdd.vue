<template>
  <div class="container-fluid bg-light">
    <h1 class="mb-4 text-center">Add Article</h1>
    <form class="mb-4" @submit.prevent="handleArticleAdd">
      <div class="mb-3">
        <label for="title" class="form-label">Title</label>
        <input
          id="title"
          v-model="articleState.title"
          type="text"
          class="form-control"
          name="title"
        />
      </div>
      <div class="mb-3">
        <label for="thumbnail" class="form-label">Thumbnail</label>
        <input
          id="thumbnail"
          type="file"
          class="form-control"
          name="thumbnail"
          @change="handleFileChange"
        />
        <img v-if="imgUrl" :src="imgUrl" class="w-100 mt-2 rounded" alt="Thumbnail" />
      </div>
      <div class="mb-3">
        <label class="form-label">Content</label>
        <QuillEditor
          v-model:content="state.content"
          :options="options"
          theme="snow"
          @editor-change="handleContentChange"
        />
      </div>
      <div class="mb-3">
        <label for="createdAt" class="form-label">Date</label>
        <input id="createdAt" type="datetime-local" class="form-control" name="createdAt" />
      </div>
      <div class="mb-3">
        <label for="category" class="form-label">Category</label>
        <select id="category" v-model="articleState.category" class="form-select" name="category">
          <option v-for="cat in props.categories" :value="cat.id">{{ cat.name }}</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="author" class="form-label">Author</label>
        <select id="author" v-model="articleState.author" class="form-select" name="author">
          <option v-for="a in props.authors" :value="a.id">{{ a.name }}</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="link" class="form-label">Link</label>
        <input id="link" v-model="articleState.link" type="text" class="form-control" name="link" />
      </div>
      <button type="submit" class="btn btn-primary">Add</button>
    </form>
  </div>
</template>

<script setup lang="ts">
// @ts-ignore
import { QuillEditor, Delta, Quill } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';
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

const toolbarOptions = [
  ['bold', 'italic', 'underline', 'strike'], // toggled buttons
  ['blockquote', 'code-block'],
  ['link', 'image', 'video', 'formula'],

  [{ header: 1 }, { header: 2 }], // custom button values
  [{ list: 'ordered' }, { list: 'bullet' }, { list: 'check' }],
  [{ script: 'sub' }, { script: 'super' }], // superscript/subscript
  [{ indent: '-1' }, { indent: '+1' }], // outdent/indent
  [{ direction: 'rtl' }], // text direction

  [{ size: ['small', false, 'large', 'huge'] }], // custom dropdown
  [{ header: [1, 2, 3, 4, 5, 6, false] }],

  [{ color: [] }, { background: [] }], // dropdown with defaults from theme
  [{ font: [] }],
  [{ align: [] }],

  ['clean'], // remove formatting button
];

const options = {
  debug: 'info',
  modules: {
    toolbar: toolbarOptions /* ["bold", "italic", "underline"] */,
  },
  placeholder: 'Compose an epic...',
  readOnly: isReadOnly,
  theme: 'snow',
};

const initialContent = `
  <h1>Main Title</h1>
  <h2>Subheading 1</h2>
  <p>Content...</p>
  <h2>Subheading 2</h2>
  <p>Content...</p>
`;

const state = reactive({ content: initialContent });
const props = defineProps(['categories', 'authors']);

const handleArticleAdd = async (e: Event) => {
  e.preventDefault();
  try {
    const formData = new FormData();

    const myHeaders = new Headers();
    myHeaders.append('Cookie', 'csrftoken=ccS5qh2RZofjzKhe6KeN51RMYOGQAb5t');

    const newImgFile = uploadedImg.value as File;

    const operations = {
      query: ADD_ARTICLE_RAW,
      variables: {
        title: articleState.title,
        content: state.content,
        thumbnail: null, // You may need to handle thumbnail separately based on your requirements
        // authorId: articleState.author,
        authorId: 1,
        categoryId: articleState.category,
      },
    };

    formData.set('operations', JSON.stringify(operations));
    formData.set('map', '{\n  "0": ["variables.thumbnail"]\n}');
    formData.set('0', newImgFile);

    const response = await fetch('http://localhost:8000/graphql/', {
      method: 'POST',
      headers: myHeaders,
      body: formData,
      redirect: 'follow',
    });

    console.log(response);
  } catch (error) {
    console.log('Error adding article', error);
  }
};

const handleFileChange = (e: Event) => {
  e.preventDefault();
  const inputEl = e.target as HTMLInputElement;
  if (inputEl.files && inputEl.files.length > 0) {
    uploadedImg.value = inputEl.files[0];
    const objectUrl = URL.createObjectURL(inputEl.files[0]);
    imgUrl.value = objectUrl;
  }
};

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
