<template>
    <h1>Category Add</h1>
    <form v-on:submit.prevent="handleCategoryAdd">
      <input type="text" v-model="categoryName" class="border border gray-300 p-2" />
      <button class="bg-gray-900 text-gray-100 p-2" type="submit">Add Category</button>
    </form>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
//   import { useMutation, gql } from '@urql/vue';
  
  const categoryName = ref('');
  
  const ADD_CATEGORY = gql`
    mutation AddCategory($name: String!) {
      createOrUpdateCategory(name: $name) {
        category {
          id
          name
        }
      }
    }
  `;
  
  const { mutate: addCategory } = useMutation(ADD_CATEGORY);
  
  const handleCategoryAdd = async () => {
    try {
      const categoryRes = await addCategory({ name: categoryName.value });
      console.log({ categoryRes });
    } catch (error) {
      console.error('Error adding category:', error);
    }
  };
  </script>