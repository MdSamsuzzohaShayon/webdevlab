<template>
  <div class="admin-layout p-0 m-0 overflow-x-hidden">
    <div class="row">
      <div v-if="state.showMenu" class="col-md-2 bg-dark text-capitalize">
        <div class="menu-wrapper w-full d-flex justify-content-end me-3 mt-3">
          <Icon
            :name="iName.close"
            :size="iDesign.smSize"
            :color="iColor.light"
            role="presentation"
            @click.prevent="handleToggleMenu(false)"
          />
        </div>
        <ul v-if="state.showMenu" class="nav flex-column">
          <li v-for="(item, index) in adminMenuList" :key="index" class="nav-item">
            <NuxtLink :to="item.link" class="nav-link text-light">
              <span class="me-2">
                <Icon :name="item.iconName" :size="iDesign.smSize" :color="iColor.light" />
              </span>
              <span>{{ item.text }}</span>
            </NuxtLink>
          </li>
        </ul>
      </div>
      <div :class="`${state.showMenu ? 'col-md-10' : 'col-md-12'} `">
        <AdminNavbar :show-menu="state.showMenu" :handle-toggle-menu="handleToggleMenu" />
        <main>
          <slot />
        </main>
      </div>
    </div>
    <AdminFooter />
  </div>
</template>

<script setup lang="ts">
import { adminMenuList } from '~/assets/js/staticData';

const state = reactive({ showMenu: false });

const handleToggleMenu = (showMenu: boolean) => {
  state.showMenu = showMenu;
};
</script>
