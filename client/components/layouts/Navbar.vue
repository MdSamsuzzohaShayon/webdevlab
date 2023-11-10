<template>
  <header class="flex items-center justify-between py-2 border-b">
    <NuxtLink to="/" class="px-2 lg:px-0 uppercase font-bold text-purple-800"> Web Dev Lab </NuxtLink>
    <ul class="inline-flex items-center">
      <li class="px-2 md:px-4">
        <NuxtLink to="/" class="text-purple-600 font-semibold hover:text-purple-500"> Home </NuxtLink>
      </li>
      <li class="px-2 md:px-4">
        <NuxtLink to="/about" class="text-gray-500 font-semibold hover:text-purple-500"> About </NuxtLink>
      </li>
      <li class="px-2 md:px-4">
        <NuxtLink to="/press" class="text-gray-500 font-semibold hover:text-purple-500"> Press </NuxtLink>
      </li>
      <li class="px-2 md:px-4">
        <NuxtLink to="/contact" class="text-gray-500 font-semibold hover:text-purple-500"> Contact </NuxtLink>
      </li>
      <li class="px-2 md:px-4 hidden md:block">
        <NuxtLink to="/login" class="text-gray-500 font-semibold hover:text-purple-500"> Login </NuxtLink>
      </li>
      <li class="px-2 md:px-4 hidden md:block">
        <NuxtLink to="/register" class="text-gray-500 font-semibold hover:text-purple-500"> Register </NuxtLink>
      </li>
    </ul>
  </header>
</template>
