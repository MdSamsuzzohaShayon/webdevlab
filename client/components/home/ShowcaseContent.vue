<template>
  <div
    class="relative flex col-span-12 bg-center bg-no-repeat bg-cover dark:bg-gray-500 xl:col-span-6 lg:col-span-5 md:col-span-9 min-h-96"
    :style="{ backgroundImage: 'url(https://source.unsplash.com/random/239x319)' }"
  >
    <span
      class="absolute px-1 pb-2 text-xs font-bold uppercase border-b-2 left-6 top-6 dark:border-violet-400 dark:text-gray-100"
      >paris, france</span
    >
    <a
      class="flex flex-col items-center justify-end p-6 text-center sm:p-8 group dark:via-transparent flex-grow-1 bg-gradient-to-b dark:from-gray-900 dark:to-gray-900"
    >
      <span class="flex items-center mb-4 space-x-2 dark:text-violet-400">
        <span class="relative flex-shrink-0 w-2 h-2 rounded-full dark:bg-violet-400">
          <span
            class="absolute flex-shrink-0 w-3 h-3 rounded-full -left-1 -top-1 animate-ping dark:bg-violet-400"
          />
        </span>
        <span class="text-sm font-bold">Live</span>
      </span>
      <h1
        rel="noopener noreferrer"
        class="font-serif text-2xl font-semibold group-hover:underline dark:text-gray-100"
      >
        Morbi mattis justo est, ac consectetur dui eleifend vitae. Donec venenatis?
      </h1>
    </a>
  </div>
</template>
