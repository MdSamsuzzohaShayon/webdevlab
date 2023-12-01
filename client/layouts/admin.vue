<template>
  <div class="flex justify-between h-full">
    <div class="w-3/12 h-screen sticky bg-gray-900 text-gray-200 items-start top-0">
      <div class="px-3">
        <ul class="flex flex-col justify-start items-start">
          <li><NuxtLink to="/admin/article">Article</NuxtLink></li>
          <li><NuxtLink to="/admin/category">Category</NuxtLink></li>
          <li><NuxtLink to="/admin/tags">Tags</NuxtLink></li>
          <li><NuxtLink to="/admin/author">Author</NuxtLink></li>
          <li><NuxtLink to="/admin/comments">Comments</NuxtLink></li>
          <li><NuxtLink to="/admin/settings">Settings</NuxtLink></li>
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
</template>
