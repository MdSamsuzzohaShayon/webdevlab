<!-- components/CategoryForm.vue -->
<template>
  <form @submit.prevent="addCategory">
    <label for="categoryName">Category Name:</label>
    <input id="categoryName" v-model="categoryName" type="text" required >

    <button type="submit">Add</button>
  </form>
</template>

<script setup lang="ts">
import { CREATE_CATEGORY } from '~/graphql/categories';

const categoryName = ref('');

const { mutate: addComment } = useMutation(CREATE_CATEGORY);
const addCategory = async () => {
  try {
    const response = await addComment({
      variables: {
        name: categoryName.value,
      },
      context: {
        clientName: 'default', // Provide the client name explicitly
      },
    });

    // Handle response as needed
    console.log('Category added successfully:', response);
  } catch (error) {
    console.error('Error adding category:', error);
  }
};
</script>
