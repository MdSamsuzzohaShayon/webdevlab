<template>
    <div class="container">
        <div class="category w-full" v-if="state.category">
            <div class="row">
                <div class="col">
                    <p class="text-uppercase">Browsing Category</p>
                    <h1>{{ state.category?.name || 'None' }}</h1>
                </div>
                <!-- <p v-for="art in state.allArticles">{{ art.title }}</p> -->
            </div>
            <div class="row">
                <div class="col-md-8">
                    <div class="row">
                        <NuxtLink class="col-12 text-decoration-none"
                            v-if="state.allArticles && state.allArticles.length > 0"
                            v-for="tutorialArticle in state.allArticles" :key="tutorialArticle.id"
                            v-bind:to="tutorialArticle.link">
                            <ArticleThumbCard :article="tutorialArticle" />
                        </NuxtLink>
                    </div>
                </div>
                <div class="col-md-4 d-flex flex-column">
                    <div class="sticky-top">
                        <h3>Top posts of the category</h3>
                        <p>Twitter feed</p>
                        <p>YouTube Feed</p>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { GET_CATEGORY_WITH_ARTICLES } from '../../graphql/categories';
import type { IArticle, ICategory, ICategoryWithArticle } from '~/types';
const route = useRoute();

interface IStateProps {
    category: ICategory | null;
    allArticles: IArticle[];
}

const state = reactive<IStateProps>({ category: null, allArticles: [] })

// Get all article of a category
try {
    const { data } = await useAsyncQuery(GET_CATEGORY_WITH_ARTICLES, { id: route.params.categoryId });
    if (data.value && data.value.categoryById) {
        console.log(data.value);
        state.category = data.value.categoryById;
        state.allArticles = data.value?.categoryById?.articleSet || [];
    }
} catch (error) {
    console.log(error);

}

</script>