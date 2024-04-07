<template>
  <div class="hidden py-2 xl:col-span-3 lg:col-span-4 md:hidden lg:block">
    <div class="mb-8 space-x-5 border-b-2 border-opacity-10 dark:border-violet-400">
      <button
        type="button"
        class="pb-5 text-xs font-bold uppercase border-b-2 dark:border-violet-400"
      >
        Latest
      </button>
      <button
        type="button"
        class="pb-5 text-xs font-bold uppercase border-b-2 dark:border-transparent dark:text-gray-400"
      >
        Popular
      </button>
    </div>
    <div class="flex flex-col divide-y divide-gray-700">
      <div class="flex px-1 py-4">
        <img
          alt=""
          class="flex-shrink-0 object-cover w-20 h-20 mr-4 dark:bg-gray-500"
          src="https://source.unsplash.com/random/244x324"
        />
        <div class="flex flex-col flex-grow">
          <a rel="noopener noreferrer" href="#" class="font-serif hover:underline"
            >Aenean ac tristique lorem, ut mollis dui.</a
          >
          <p class="mt-auto text-xs dark:text-gray-400">
            5 minutes ago
            <a
              rel="noopener noreferrer"
              href="#"
              class="block dark:text-blue-400 lg:ml-2 lg:inline hover:underline"
              >Politics</a
            >
          </p>
        </div>
      </div>
      <div class="flex px-1 py-4">
        <img
          alt=""
          class="flex-shrink-0 object-cover w-20 h-20 mr-4 dark:bg-gray-500"
          src="https://source.unsplash.com/random/245x325"
        />
        <div class="flex flex-col flex-grow">
          <a rel="noopener noreferrer" href="#" class="font-serif hover:underline"
            >Nulla consectetur efficitur.</a
          >
          <p class="mt-auto text-xs dark:text-gray-400">
            14 minutes ago
            <a
              rel="noopener noreferrer"
              href="#"
              class="block dark:text-blue-400 lg:ml-2 lg:inline hover:underline"
              >Sports</a
            >
          </p>
        </div>
      </div>
      <div class="flex px-1 py-4">
        <img
          alt=""
          class="flex-shrink-0 object-cover w-20 h-20 mr-4 dark:bg-gray-500"
          src="https://source.unsplash.com/random/246x326"
        />
        <div class="flex flex-col flex-grow">
          <a rel="noopener noreferrer" href="#" class="font-serif hover:underline"
            >Vitae semper augue purus tincidunt libero.</a
          >
          <p class="mt-auto text-xs dark:text-gray-400">
            22 minutes ago
            <a
              rel="noopener noreferrer"
              href="#"
              class="block dark:text-blue-400 lg:ml-2 lg:inline hover:underline"
              >World</a
            >
          </p>
        </div>
      </div>
      <div class="flex px-1 py-4">
        <img
          alt=""
          class="flex-shrink-0 object-cover w-20 h-20 mr-4 dark:bg-gray-500"
          src="https://source.unsplash.com/random/247x327"
        />
        <div class="flex flex-col flex-grow">
          <a rel="noopener noreferrer" href="#" class="font-serif hover:underline"
            >Suspendisse potenti.</a
          >
          <p class="mt-auto text-xs dark:text-gray-400">
            37 minutes ago
            <a
              rel="noopener noreferrer"
              href="#"
              class="block dark:text-blue-400 lg:ml-2 lg:inline hover:underline"
              >Business</a
            >
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
