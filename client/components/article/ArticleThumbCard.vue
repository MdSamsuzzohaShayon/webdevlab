<template>
    <div class="card mb-3" style="width: 100%;">
        <div class="row g-0">
            <div class="col-md-4">
                <CldImage v-if="props.article.thumbnail" :src="props.article.thumbnail" width="800" height="800"
                    class="card-img img-fluid rounded-start" :alt="props.article.title" />
            </div>
            <div class="col-md-8">
                <div class="card-body">
                    <h5 class="card-title">{{ props.article.title }}</h5>
                    <p class="card-text">{{ shortDesc(props.article.content, 200) }}</p>
                    <p class="card-text"><small class="text-body-secondary">{{
                    props.article.createdAt &&
                    formatReadableDate(props.article.createdAt)
                            }}</small></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>

const props = defineProps(['article']);
</script>