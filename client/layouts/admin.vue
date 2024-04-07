<template>
  <div>
    <div class="flex justify-between h-full">
      <div class="w-3/12 h-screen sticky bg-primary items-start top-0">
        <div class="px-3">
          <ul class="flex flex-col justify-start items-start mt-4 gap-y-4">
            <li v-for="item in adminMenuList" :key="item.id">
              <NuxtLink :to="item.link">
                <span class="mr-2">
                  <Icon :name="item.iconName" :size="is" color="white" />
                </span>
                <span>{{ item.text }}</span>
              </NuxtLink>
            </li>
          </ul>
        </div>
      </div>
      <div class="w-9/12 text-gray-900">
        <div class="px-3">
          <AdminNavbar />
          <slot />
        </div>
      </div>
    </div>
    <AdminFooter />
  </div>
</template>

<script setup lang="ts">
import { adminMenuList } from '~/assets/js/staticData';

console.log(adminMenuList);
</script>
