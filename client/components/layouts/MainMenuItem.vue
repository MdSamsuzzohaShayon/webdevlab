<template>
    <nav :class="`w-full flex justify-between items-center ${cmip}`">
          <ul class="mt-4 md:mt-0 w-full md:w-fit md:flex md:gap-x-2">
            <li v-for="item in props.menuList" :class="`w-full leading-10 ${hbd} md:border-b-0`">
              <NuxtLink :to="item.link" class="">{{ item.text }}</NuxtLink>
            </li>
          </ul>
        </nav>
</template>


<script setup lang="ts">
import type { IMenuItem } from '~/types';

const props = defineProps({
    menuList: Array as PropType<IMenuItem[]>
})

</script>