<!-- components/CategoryForm.vue -->
<template>
  <form @submit.prevent="addCategory" class="container mt-5">
    <div class="form-group">
      <label for="categoryName">Category Name:</label>
      <input
        id="categoryName"
        v-model="categoryName"
        type="text"
        class="form-control"
        required
        placeholder="Enter category name"
      >
    </div>
    <button type="submit" class="btn btn-primary mt-3">Add Category</button>
  </form>
</template>

<script setup lang="ts">
import { CREATE_CATEGORY } from '~/graphql/categories';

const categoryName = ref('');

const { mutate: addArticleCategory } = useMutation(CREATE_CATEGORY);
const addCategory = async () => {
  try {
    const response = await addArticleCategory({
      name: categoryName.value,
    });

    // Handle response as needed
    console.log('Category added successfully:', response);
  } catch (error) {
    console.error('Error adding category:', error);
  }
};
</script>
