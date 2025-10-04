<template>
  <div
    class="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-900 dark:to-slate-800"
  >
    <!-- Animated Background Elements -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none z-0">
      <div
        class="absolute -top-40 -right-40 w-80 h-80 bg-[#8A2BE2]/10 rounded-full mix-blend-multiply dark:mix-blend-screen filter blur-3xl animate-float-slow"
      ></div>
      <div
        class="absolute -bottom-40 -left-40 w-80 h-80 bg-[#20D9C4]/10 rounded-full mix-blend-multiply dark:mix-blend-screen filter blur-3xl animate-float-medium"
        style="animation-delay: 2s"
      ></div>
      <div
        class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-[#D6E74E]/10 rounded-full mix-blend-multiply dark:mix-blend-screen filter blur-3xl animate-float-fast"
        style="animation-delay: 4s"
      ></div>

      <!-- Grid Pattern -->
      <div class="absolute inset-0 opacity-5">
        <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <pattern
              id="smallGrid"
              width="40"
              height="40"
              patternUnits="userSpaceOnUse"
            >
              <path
                d="M 40 0 L 0 0 0 40"
                fill="none"
                stroke="#8A2BE2"
                stroke-width="1"
              />
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#smallGrid)" />
        </svg>
      </div>
    </div>

    <!-- Header -->
    <header
      class="sticky top-0 z-50 backdrop-blur-md bg-white/80 dark:bg-slate-900/80 border-b border-slate-200/50 dark:border-slate-700/50 transition-all duration-500"
    >
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center py-4">
          <NuxtLink
            to="/"
            class="flex items-center space-x-2 group cursor-pointer"
          >
            <NuxtImg
              src="/images/logo-light.png"
              class="w-16 h-16 rounded-lg"
            />
          </NuxtLink>

          <!-- Navigation -->
          <nav class="hidden md:flex space-x-8">
            <a
              href="#"
              class="text-slate-600 dark:text-slate-300 hover:text-[#8A2BE2] dark:hover:text-[#20D9C4] font-medium transition-all duration-300 hover:scale-105 relative group"
            >
              Home
              <span
                class="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] group-hover:w-full transition-all duration-300"
              ></span>
            </a>
            <a
              href="#"
              class="text-slate-600 dark:text-slate-300 hover:text-[#8A2BE2] dark:hover:text-[#20D9C4] font-medium transition-all duration-300 hover:scale-105 relative group"
            >
              Articles
              <span
                class="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] group-hover:w-full transition-all duration-300"
              ></span>
            </a>
            <a
              href="#"
              class="text-slate-600 dark:text-slate-300 hover:text-[#8A2BE2] dark:hover:text-[#20D9C4] font-medium transition-all duration-300 hover:scale-105 relative group"
            >
              Topics
              <span
                class="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] group-hover:w-full transition-all duration-300"
              ></span>
            </a>
            <a
              href="#"
              class="text-slate-600 dark:text-slate-300 hover:text-[#8A2BE2] dark:hover:text-[#20D9C4] font-medium transition-all duration-300 hover:scale-105 relative group"
            >
              About
              <span
                class="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] group-hover:w-full transition-all duration-300"
              ></span>
            </a>
          </nav>

          <!-- Theme Toggle & CTA -->
          <div class="flex items-center space-x-4">
            <button
              @click="toggleTheme"
              class="p-2 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-all duration-300 transform hover:rotate-180"
            >
              <svg
                v-if="darkMode"
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"
                  clip-rule="evenodd"
                />
              </svg>
              <svg
                v-else
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"
                />
              </svg>
            </button>
            <button
              class="px-4 py-2 bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] text-white font-medium rounded-lg hover:from-[#7A1BD2] hover:to-[#2A56EF] transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl relative overflow-hidden group"
            >
              <span class="relative z-10">Subscribe</span>
              <div
                class="absolute inset-0 bg-gradient-to-r from-[#20D9C4] to-[#D6E74E] transform scale-x-0 group-hover:scale-x-100 transition-transform duration-300 origin-left"
              ></div>
            </button>
          </div>
        </div>
      </div>
    </header>

    <!-- Hero Section -->
    <section class="relative py-16 md:py-24 overflow-hidden z-10">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <div class="text-center max-w-3xl mx-auto animate-fade-in-up">
          <!-- Badge -->
          <div
            class="inline-flex items-center px-4 py-2 rounded-full bg-[#8A2BE2]/10 text-[#8A2BE2] dark:text-[#20D9C4] text-sm font-medium mb-8 backdrop-blur-sm transform hover:scale-105 transition-all duration-300 animate-bounce-subtle"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-4 w-4 mr-2"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M13 10V3L4 14h7v7l9-11h-7z"
              />
            </svg>
            Latest insights on technology and development
          </div>

          <h1
            class="text-4xl md:text-6xl font-bold text-slate-900 dark:text-white mb-6 animate-fade-in-up"
            style="animation-delay: 0.2s"
          >
            WebDevLab
            <span
              class="text-transparent bg-clip-text bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] animate-text-shimmer"
              >Blog</span
            >
          </h1>
          <p
            class="text-xl text-slate-600 dark:text-slate-300 mb-10 max-w-2xl mx-auto animate-fade-in-up"
            style="animation-delay: 0.4s"
          >
            Explore cutting-edge insights, tutorials, and trends in web
            development, AI, blockchain, and emerging technologies.
          </p>

          <!-- Search and Filter -->
          <div
            class="max-w-2xl mx-auto mb-12 animate-fade-in-up"
            style="animation-delay: 0.6s"
          >
            <div class="relative">
              <input
                type="text"
                placeholder="Search articles, tutorials, and guides..."
                class="w-full px-6 py-4 rounded-xl border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-[#8A2BE2] bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-sm transition-all duration-300 focus:scale-105"
                v-model="searchQuery"
              />
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6 text-slate-400 absolute right-4 top-1/2 transform -translate-y-1/2"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                />
              </svg>
            </div>

            <!-- Category Filter -->
            <div class="flex flex-wrap justify-center gap-3 mt-6">
              <button
                v-for="(category, index) in categories"
                :key="category"
                @click="toggleCategory(category)"
                :class="{
                  'bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] text-white shadow-md':
                    selectedCategories.includes(category),
                  'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-700 border border-slate-200 dark:border-slate-700':
                    !selectedCategories.includes(category),
                }"
                class="px-4 py-2 rounded-full transition-all duration-300 transform hover:scale-105 flex items-center animate-fade-in-up"
                :style="`animation-delay: ${0.8 + index * 0.1}s`"
              >
                <span v-if="category === 'AI'" class="mr-1">🤖</span>
                <span v-if="category === 'Web3'" class="mr-1">⛓️</span>
                <span v-if="category === 'Mobile'" class="mr-1">📱</span>
                <span v-if="category === 'Backend'" class="mr-1">⚙️</span>
                <span v-if="category === 'Full Stack'" class="mr-1">🔄</span>
                {{ category }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Blog Posts -->
    <section class="py-12 pb-20 relative z-10">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Section Header -->
        <div
          class="flex flex-col md:flex-row md:items-end justify-between mb-12 animate-fade-in-up"
        >
          <div>
            <h2 class="text-3xl font-bold text-slate-900 dark:text-white">
              Latest Articles
            </h2>
            <p class="text-slate-600 dark:text-slate-400 mt-2">
              Insights and tutorials from industry experts
            </p>
          </div>
          <div
            class="mt-4 md:mt-0 flex items-center space-x-2 text-sm text-slate-500 dark:text-slate-400"
          >
            <span>Sort by:</span>
            <select
              class="bg-transparent border-0 focus:ring-0 text-slate-700 dark:text-slate-300 rounded-lg px-3 py-1 bg-slate-100 dark:bg-slate-800 transition-all duration-300 hover:bg-slate-200 dark:hover:bg-slate-700"
            >
              <option>Latest</option>
              <option>Popular</option>
              <option>Trending</option>
            </select>
          </div>
        </div>

        <!-- Featured Post -->
        <div v-if="filteredPosts.length > 0" class="mb-16 animate-fade-in-up">
          <div
            class="bg-gradient-to-r from-slate-800 to-slate-900 dark:from-slate-700 dark:to-slate-800 rounded-2xl overflow-hidden shadow-xl transform hover:scale-[1.02] transition-all duration-500 group"
          >
            <div class="grid grid-cols-1 lg:grid-cols-2">
              <div class="p-8 md:p-12 flex flex-col justify-center">
                <div class="flex items-center text-sm text-slate-300 mb-4">
                  <span
                    class="px-3 py-1 bg-[#8A2BE2]/20 text-[#20D9C4] rounded-full text-xs font-medium"
                    >{{ filteredPosts[0].category }}</span
                  >
                  <span class="mx-3">•</span>
                  <span>{{ filteredPosts[0].date }}</span>
                  <span class="mx-3">•</span>
                  <span>{{ filteredPosts[0].readTime }} read</span>
                </div>

                <h3
                  class="text-2xl md:text-3xl font-bold text-white mb-4 group-hover:text-[#20D9C4] transition-colors duration-300"
                >
                  {{ filteredPosts[0].title }}
                </h3>

                <p class="text-slate-300 mb-6">
                  {{ filteredPosts[0].excerpt }}
                </p>

                <div class="flex items-center justify-between">
                  <div class="flex items-center">
                    <div
                      class="w-10 h-10 rounded-full bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] mr-3 flex items-center justify-center text-white font-bold transform group-hover:scale-110 transition-transform duration-300"
                    >
                      {{ filteredPosts[0].author.charAt(0) }}
                    </div>
                    <span class="text-sm font-medium text-white">{{
                      filteredPosts[0].author
                    }}</span>
                  </div>

                  <NuxtLink
                    :to="`/${filteredPosts[0].slug}`"
                    class="bg-white text-slate-900 font-medium px-5 py-2.5 rounded-lg hover:bg-[#D6E74E] transition-all duration-300 transform group-hover:scale-105 flex items-center shadow-lg"
                  >
                    Read article
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-4 w-4 ml-2 transform group-hover:translate-x-1 transition-transform duration-300"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M14 5l7 7m0 0l-7 7m7-7H3"
                      />
                    </svg>
                  </NuxtLink>
                </div>
              </div>
              <div class="relative min-h-80 lg:min-h-0 overflow-hidden">
                <div
                  class="absolute inset-0 bg-gradient-to-r from-[#8A2BE2]/20 to-[#3366FF]/20 group-hover:from-[#8A2BE2]/30 group-hover:to-[#3366FF]/30 transition-all duration-500"
                ></div>
                <div
                  class="absolute inset-0 flex items-center justify-center transform group-hover:scale-110 transition-transform duration-500"
                >
                  <div class="text-6xl opacity-20">
                    <span v-if="filteredPosts[0].category === 'AI'">🤖</span>
                    <span v-else-if="filteredPosts[0].category === 'Web3'"
                      >⛓️</span
                    >
                    <span v-else-if="filteredPosts[0].category === 'Mobile'"
                      >📱</span
                    >
                    <span v-else-if="filteredPosts[0].category === 'Backend'"
                      >⚙️</span
                    >
                    <span v-else-if="filteredPosts[0].category === 'Full Stack'"
                      >🔄</span
                    >
                    <span v-else>📝</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Posts Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <article
            v-for="(post, index) in filteredPosts.slice(1)"
            :key="post.id"
            class="card group overflow-hidden hover:shadow-2xl transition-all duration-500 bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 animate-fade-in-up"
            :style="`animation-delay: ${index * 0.1}s`"
          >
            <div class="relative overflow-hidden">
              <div
                class="aspect-video w-full bg-gradient-to-r relative overflow-hidden"
                :class="getPostGradient(post.category)"
              >
                <div
                  class="absolute inset-0 bg-black/10 group-hover:bg-black/20 transition-all duration-300"
                ></div>
                <div
                  class="absolute top-4 left-4 transform group-hover:scale-110 transition-transform duration-300"
                >
                  <span
                    class="px-3 py-1 text-xs font-medium rounded-full text-white bg-black/40 backdrop-blur-sm"
                  >
                    {{ post.category }}
                  </span>
                </div>
                <div
                  class="absolute bottom-4 right-4 text-white text-4xl opacity-20 transform group-hover:scale-125 group-hover:opacity-30 transition-all duration-500"
                >
                  <span v-if="post.category === 'AI'">🤖</span>
                  <span v-else-if="post.category === 'Web3'">⛓️</span>
                  <span v-else-if="post.category === 'Mobile'">📱</span>
                  <span v-else-if="post.category === 'Backend'">⚙️</span>
                  <span v-else-if="post.category === 'Full Stack'">🔄</span>
                  <span v-else>📝</span>
                </div>
              </div>
            </div>

            <div class="p-6">
              <div
                class="flex items-center text-sm text-slate-500 dark:text-slate-400 mb-3"
              >
                <span>{{ post.date }}</span>
                <span class="mx-2">•</span>
                <span>{{ post.readTime }} read</span>
              </div>

              <h3
                class="text-xl font-bold text-slate-900 dark:text-white mb-3 group-hover:text-[#8A2BE2] dark:group-hover:text-[#20D9C4] transition-colors duration-300 line-clamp-2"
              >
                {{ post.title }}
              </h3>

              <p class="text-slate-600 dark:text-slate-300 mb-4 line-clamp-3">
                {{ post.excerpt }}
              </p>

              <div
                class="flex items-center justify-between pt-4 border-t border-slate-100 dark:border-slate-700"
              >
                <div class="flex items-center">
                  <div
                    class="w-8 h-8 rounded-full bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] mr-3 flex items-center justify-center text-white text-xs font-bold transform group-hover:scale-110 transition-transform duration-300"
                  >
                    {{ post.author.charAt(0) }}
                  </div>
                  <span
                    class="text-sm font-medium text-slate-700 dark:text-slate-300"
                    >{{ post.author }}</span
                  >
                </div>

                <NuxtLink
                  :to="`/${post.slug}`"
                  class="text-[#8A2BE2] dark:text-[#20D9C4] hover:text-[#3366FF] dark:hover:text-[#D6E74E] font-medium flex items-center transition-all duration-300 transform group-hover:translate-x-1 group/link"
                >
                  Read
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-4 w-4 ml-1 transform group-hover/link:translate-x-1 transition-transform duration-300"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M14 5l7 7m0 0l-7 7m7-7H3"
                    />
                  </svg>
                </NuxtLink>
              </div>
            </div>
          </article>
        </div>

        <!-- Empty state -->
        <div
          v-if="filteredPosts.length === 0"
          class="text-center py-16 animate-fade-in-up"
        >
          <div class="max-w-md mx-auto">
            <div
              class="w-24 h-24 mx-auto mb-6 rounded-full bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] flex items-center justify-center text-white animate-pulse"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-10 w-10"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
            </div>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-2">
              No articles found
            </h3>
            <p class="text-slate-600 dark:text-slate-400 mb-6">
              Try adjusting your search or filter criteria
            </p>
            <button
              @click="resetFilters"
              class="px-4 py-2 bg-[#8A2BE2]/10 text-[#8A2BE2] dark:text-[#20D9C4] font-medium rounded-lg hover:bg-[#8A2BE2]/20 transition-all duration-300 transform hover:scale-105"
            >
              Reset filters
            </button>
          </div>
        </div>

        <!-- Load More Button -->
        <div
          v-if="filteredPosts.length > 0"
          class="text-center mt-12 animate-fade-in-up"
        >
          <button
            class="px-6 py-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 font-medium rounded-lg hover:bg-[#D6E74E] dark:hover:bg-[#3366FF] hover:text-slate-900 dark:hover:text-white transition-all duration-300 transform hover:scale-105 shadow-sm hover:shadow-md"
          >
            Load more articles
          </button>
        </div>
      </div>
    </section>

    <!-- Newsletter CTA -->
    <section
      class="py-16 bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] relative overflow-hidden"
    >
      <!-- Animated Background -->
      <div class="absolute inset-0 overflow-hidden">
        <div
          class="absolute -top-20 -right-20 w-40 h-40 bg-[#20D9C4]/20 rounded-full mix-blend-screen filter blur-xl animate-float-slow"
        ></div>
        <div
          class="absolute -bottom-20 -left-20 w-40 h-40 bg-[#D6E74E]/20 rounded-full mix-blend-screen filter blur-xl animate-float-medium"
          style="animation-delay: 2s"
        ></div>
        <div
          class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-60 h-60 bg-white/10 rounded-full mix-blend-screen filter blur-xl animate-float-fast"
          style="animation-delay: 4s"
        ></div>
      </div>

      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative">
        <div
          class="inline-flex items-center px-4 py-2 rounded-full bg-white/10 text-white text-sm font-medium mb-6 backdrop-blur-sm transform hover:scale-105 transition-all duration-300"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-4 w-4 mr-2"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
            />
          </svg>
          Stay updated with our newsletter
        </div>

        <h2 class="text-3xl font-bold text-white mb-4 animate-fade-in-up">
          Never Miss an Article
        </h2>
        <p
          class="text-indigo-100 text-lg mb-8 max-w-2xl mx-auto animate-fade-in-up"
          style="animation-delay: 0.2s"
        >
          Get the latest articles on web development, AI, blockchain, and more
          delivered directly to your inbox.
        </p>
        <div
          class="flex flex-col sm:flex-row gap-4 max-w-lg mx-auto animate-fade-in-up"
          style="animation-delay: 0.4s"
        >
          <input
            type="email"
            placeholder="Enter your email"
            class="flex-1 px-4 py-3 rounded-lg border-0 focus:outline-none focus:ring-2 focus:ring-white/30 bg-white/10 backdrop-blur-sm text-white placeholder-indigo-200 transition-all duration-300 focus:scale-105"
          />
          <button
            class="bg-[#D6E74E] text-slate-900 font-semibold px-8 py-3 rounded-lg hover:bg-[#20D9C4] hover:text-white transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl relative overflow-hidden group"
          >
            <span class="relative z-10">Subscribe</span>
            <div
              class="absolute inset-0 bg-gradient-to-r from-[#20D9C4] to-[#3366FF] transform scale-x-0 group-hover:scale-x-100 transition-transform duration-300 origin-left"
            ></div>
          </button>
        </div>
        <p
          class="text-indigo-200 text-sm mt-4 animate-fade-in-up"
          style="animation-delay: 0.6s"
        >
          No spam, unsubscribe at any time
        </p>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-800 text-slate-300 py-12 relative z-10">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div class="md:col-span-2">
            <div class="flex items-center space-x-2 mb-4 group cursor-pointer">
              <div
                class="w-8 h-8 rounded-lg bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] flex items-center justify-center transform group-hover:scale-110 transition-transform duration-300"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-white"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"
                  />
                </svg>
              </div>
              <span
                class="text-xl font-bold text-white transform group-hover:translate-x-1 transition-transform duration-300"
                >WebDevLab</span
              >
            </div>
            <p class="mb-6 max-w-md">
              A platform for developers to explore cutting-edge technologies,
              share knowledge, and grow together in the ever-evolving world of
              web development.
            </p>
            <div class="flex space-x-4">
              <a
                href="#"
                class="w-10 h-10 rounded-full bg-slate-700 flex items-center justify-center hover:bg-[#8A2BE2] transition-all duration-300 transform hover:scale-110 hover:-translate-y-1"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path
                    d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"
                  ></path>
                </svg>
              </a>
              <a
                href="#"
                class="w-10 h-10 rounded-full bg-slate-700 flex items-center justify-center hover:bg-[#3366FF] transition-all duration-300 transform hover:scale-110 hover:-translate-y-1"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path
                    d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"
                  ></path>
                </svg>
              </a>
              <a
                href="#"
                class="w-10 h-10 rounded-full bg-slate-700 flex items-center justify-center hover:bg-[#20D9C4] transition-all duration-300 transform hover:scale-110 hover:-translate-y-1"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path
                    d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"
                  ></path>
                </svg>
              </a>
            </div>
          </div>

          <div>
            <h3 class="text-white font-semibold mb-4">Topics</h3>
            <ul class="space-y-2">
              <li>
                <a
                  href="#"
                  class="hover:text-[#20D9C4] transition-colors duration-300"
                  >Web Development</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-[#20D9C4] transition-colors duration-300"
                  >AI & Machine Learning</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-[#20D9C4] transition-colors duration-300"
                  >Web3 & Blockchain</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-[#20D9C4] transition-colors duration-300"
                  >Mobile Development</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-[#20D9C4] transition-colors duration-300"
                  >Backend Systems</a
                >
              </li>
            </ul>
          </div>

          <div>
            <h3 class="text-white font-semibold mb-4">Company</h3>
            <ul class="space-y-2">
              <li>
                <a
                  href="#"
                  class="hover:text-[#20D9C4] transition-colors duration-300"
                  >About Us</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-[#20D9C4] transition-colors duration-300"
                  >Careers</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-[#20D9C4] transition-colors duration-300"
                  >Contact</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-[#20D9C4] transition-colors duration-300"
                  >Privacy Policy</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-[#20D9C4] transition-colors duration-300"
                  >Terms of Service</a
                >
              </li>
            </ul>
          </div>
        </div>

        <div
          class="border-t border-slate-700 mt-8 pt-8 text-sm text-slate-400 flex flex-col md:flex-row justify-between"
        >
          <div class="mb-4 md:mb-0">© 2023 WebDevLab. All rights reserved.</div>
          <div>
            Made with <span class="text-[#D6E74E] animate-pulse">❤️</span> for
            the developer community
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
// Blog posts data
const posts = [
  {
    id: 1,
    title: "Understanding Web3: The Decentralized Future of the Internet",
    excerpt:
      "Explore how Web3 is transforming digital interactions through blockchain, decentralization, and token-based economics.",
    category: "Web3",
    date: "May 15, 2023",
    readTime: "8 min",
    author: "Sarah Johnson",
    slug: "understanding-web3-decentralized-future",
    gradient: "from-[#8A2BE2] to-[#3366FF]",
  },
  {
    id: 2,
    title: "AI-Powered Development: Revolutionizing How We Build Software",
    excerpt:
      "Discover how artificial intelligence is changing the landscape of software development with code generation and automated testing.",
    category: "AI",
    date: "April 28, 2023",
    readTime: "10 min",
    author: "Michael Chen",
    slug: "ai-powered-development-revolution",
    gradient: "from-[#20D9C4] to-[#3366FF]",
  },
  {
    id: 3,
    title: "Mobile Development in 2023: Cross-Platform vs Native",
    excerpt:
      "A comprehensive comparison of development approaches for mobile applications in the current ecosystem.",
    category: "Mobile",
    date: "April 12, 2023",
    readTime: "6 min",
    author: "Jessica Williams",
    slug: "mobile-development-2023-cross-platform-vs-native",
    gradient: "from-[#D6E74E] to-[#20D9C4]",
  },
  {
    id: 4,
    title: "Scaling Backend Systems: Strategies for High Traffic Applications",
    excerpt:
      "Learn essential techniques for building backend systems that can handle millions of users without breaking a sweat.",
    category: "Backend",
    date: "March 30, 2023",
    readTime: "12 min",
    author: "David Kim",
    slug: "scaling-backend-systems-strategies",
    gradient: "from-[#8A2BE2] to-[#D6E74E]",
  },
  {
    id: 5,
    title: "The Complete Full Stack Developer Roadmap 2023",
    excerpt:
      "A step-by-step guide to becoming a proficient full stack developer with the most relevant technologies this year.",
    category: "Full Stack",
    date: "March 18, 2023",
    readTime: "15 min",
    author: "Alex Rodriguez",
    slug: "complete-full-stack-developer-roadmap-2023",
    gradient: "from-[#3366FF] to-[#20D9C4]",
  },
  {
    id: 6,
    title: "Smart Contracts 101: Building on Ethereum and Solidity",
    excerpt:
      "An introduction to creating and deploying smart contracts on the Ethereum blockchain using Solidity.",
    category: "Web3",
    date: "March 5, 2023",
    readTime: "9 min",
    author: "Emma Thompson",
    slug: "smart-contracts-101-ethereum-solidity",
    gradient: "from-[#8A2BE2] to-[#3366FF]",
  },
];

// Categories
const categories = ["All", "Web3", "AI", "Mobile", "Backend", "Full Stack"];

// Reactive state
const searchQuery = ref("");
const selectedCategories = ref(["All"]);
const darkMode = ref(false);

// Filter posts based on search and categories
const filteredPosts = computed(() => {
  return posts.filter((post) => {
    const matchesSearch =
      post.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      post.excerpt.toLowerCase().includes(searchQuery.value.toLowerCase());

    const matchesCategory =
      selectedCategories.value.includes("All") ||
      selectedCategories.value.includes(post.category);

    return matchesSearch && matchesCategory;
  });
});

// Get gradient based on category
function getPostGradient(category) {
  const gradients = {
    Web3: "from-[#8A2BE2] to-[#3366FF]",
    AI: "from-[#20D9C4] to-[#3366FF]",
    Mobile: "from-[#D6E74E] to-[#20D9C4]",
    Backend: "from-[#8A2BE2] to-[#D6E74E]",
    "Full Stack": "from-[#3366FF] to-[#20D9C4]",
  };
  return gradients[category] || "from-[#8A2BE2] to-[#3366FF]";
}

// Toggle category filter
function toggleCategory(category) {
  if (category === "All") {
    selectedCategories.value = ["All"];
    return;
  }

  // Remove 'All' if other categories are selected
  if (selectedCategories.value.includes("All")) {
    selectedCategories.value = selectedCategories.value.filter(
      (c) => c !== "All"
    );
  }

  if (selectedCategories.value.includes(category)) {
    selectedCategories.value = selectedCategories.value.filter(
      (c) => c !== category
    );

    // If no categories selected, revert to 'All'
    if (selectedCategories.value.length === 0) {
      selectedCategories.value = ["All"];
    }
  } else {
    selectedCategories.value.push(category);
  }
}

// Reset all filters
function resetFilters() {
  searchQuery.value = "";
  selectedCategories.value = ["All"];
}

// Toggle dark mode
function toggleTheme() {
  darkMode.value = !darkMode.value;
  if (darkMode.value) {
    document.documentElement.classList.add("dark");
  } else {
    document.documentElement.classList.remove("dark");
  }
}

// Set page metadata
useHead({
  title: "Blog - WebDevLab",
  meta: [
    {
      name: "description",
      content:
        "Explore articles on Web3, AI, mobile development, backend scaling, and full stack development at WebDevLab.",
    },
  ],
});
</script>

<style scoped>
.card {
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05),
    0 2px 4px -1px rgba(0, 0, 0, 0.03);
}

.card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Custom Animations */
@keyframes float-slow {
  0%,
  100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-20px) rotate(5deg);
  }
}

@keyframes float-medium {
  0%,
  100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-15px) rotate(-3deg);
  }
}

@keyframes float-fast {
  0%,
  100% {
    transform: translateY(0) scale(1);
  }
  50% {
    transform: translateY(-10px) scale(1.05);
  }
}

@keyframes fade-in-up {
  0% {
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes bounce-subtle {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-5px);
  }
}

@keyframes text-shimmer {
  0% {
    background-position: -200% center;
  }
  100% {
    background-position: 200% center;
  }
}

.animate-float-slow {
  animation: float-slow 10s ease-in-out infinite;
}

.animate-float-medium {
  animation: float-medium 8s ease-in-out infinite;
}

.animate-float-fast {
  animation: float-fast 6s ease-in-out infinite;
}

.animate-fade-in-up {
  animation: fade-in-up 0.8s ease-out forwards;
  opacity: 0;
}

.animate-bounce-subtle {
  animation: bounce-subtle 2s ease-in-out infinite;
}

.animate-text-shimmer {
  background: linear-gradient(
    90deg,
    #8a2be2,
    #3366ff,
    #20d9c4,
    #d6e74e,
    #8a2be2
  );
  background-size: 200% auto;
  animation: text-shimmer 3s linear infinite;
  -webkit-background-clip: text;
  background-clip: text;
}
</style>
