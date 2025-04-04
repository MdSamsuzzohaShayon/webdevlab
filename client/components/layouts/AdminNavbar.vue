<template>
  <header v-if="!props.showMenu" class="admin-header">
    <nav class="navbar">
      <div class="container-fluid">
        <div v-if="!props.showMenu" class="w-full menu-wrapper d-flex justify-centent-start">
          <Icon
            :name="iName.menu"
            :size="iDesign.smSize"
            :color="iColor.dark"
            role="presentation"
            @click.prevent="props.handleToggleMenu(true)"
          />
        </div>
        <a class="navbar-brand" href="#">
          <img
            src="/logo.png"
            alt="Logo"
            width="30"
            height="24"
            class="d-inline-block align-text-top"
          >
          WebDevLab
        </a>
      </div>
    </nav>
  </header>
</template>

<script lang="ts" setup>
const props = defineProps(['showMenu', 'handleToggleMenu']);
</script>
