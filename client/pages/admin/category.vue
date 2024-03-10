<template>
  <ClientOnly>
    <h1>Category</h1>
    <Category v-for="cat in data.allCategories" v-bind:key="cat.id" v-bind:category="cat" />
    <CategoryAdd />
  </ClientOnly>
</template>

<script setup lang="ts">
definePageMeta({
  layout: "admin",
});

const query = gql`
  query AllCategories {
    allCategories {
      id
      name
    }
  }
`;


interface ICategory{
  id: number;
  name: string;
}

type Category={
  allCategories: ICategory[];
}
const { data } = await useAsyncQuery<Category>(query);
console.log(data.value);


</script>
