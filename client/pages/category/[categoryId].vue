<template>
    <div class="container">
        <!-- <ArticleExpand :post-link="$route.params.categoryId" /> -->
         List of article
         <!-- <p v-for="art in state.category.articleSet">{{ art.name }}</p> -->
    </div>
</template>

<script setup lang="ts">
import { GET_CATEGORY_WITH_ARTICLES } from '../../graphql/categories';
import type { ICategoryWithArticle } from '~/types';
const route = useRoute();

interface IStateProps{
    category: ICategoryWithArticle;
}

const state = reactive({category: null})

// Get all article of a category
try {
    const { data } = await useAsyncQuery(GET_CATEGORY_WITH_ARTICLES, {variables: {id: route.params.categoryId}});
    console.log(data.value);
    if(data.value && data.value.categoryById){
        state.category = data.value;
    }
} catch (error) {
    console.log(error);
    
}

</script>