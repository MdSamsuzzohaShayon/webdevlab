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
    </div>

    <!-- Header -->
    <header
      class="sticky top-0 z-50 backdrop-blur-md bg-white/80 dark:bg-slate-900/80 border-b border-slate-200/50 dark:border-slate-700/50 transition-all duration-500"
    >
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center py-4">
          <!-- Logo -->
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
            <NuxtLink
              to="/"
              class="text-slate-600 dark:text-slate-300 hover:text-[#8A2BE2] dark:hover:text-[#20D9C4] font-medium transition-all duration-300 hover:scale-105 relative group"
            >
              Home
              <span
                class="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] group-hover:w-full transition-all duration-300"
              ></span>
            </NuxtLink>
            <NuxtLink
              to="/blog"
              class="text-slate-600 dark:text-slate-300 hover:text-[#8A2BE2] dark:hover:text-[#20D9C4] font-medium transition-all duration-300 hover:scale-105 relative group"
            >
              Articles
              <span
                class="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] group-hover:w-full transition-all duration-300"
              ></span>
            </NuxtLink>
            <NuxtLink
              to="/services"
              class="text-slate-600 dark:text-slate-300 hover:text-[#8A2BE2] dark:hover:text-[#20D9C4] font-medium transition-all duration-300 hover:scale-105 relative group"
            >
              Services
              <span
                class="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] group-hover:w-full transition-all duration-300"
              ></span>
            </NuxtLink>
          </nav>

          <!-- Theme Toggle -->
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
          </div>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="relative z-10">
      <!-- Article Hero Section -->
      <section
        class="relative py-16 md:py-20 bg-gradient-to-br from-white/50 to-slate-100/50 dark:from-slate-800/50 dark:to-slate-900/50 backdrop-blur-sm"
      >
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center">
            <!-- Category Badge -->
            <div
              class="inline-flex items-center px-4 py-2 rounded-full bg-[#8A2BE2]/10 text-[#8A2BE2] dark:text-[#20D9C4] text-sm font-medium mb-6 backdrop-blur-sm border border-[#8A2BE2]/20"
            >
              <span class="w-2 h-2 bg-[#8A2BE2] rounded-full mr-2"></span>
              {{ post.category }}
            </div>

            <!-- Title -->
            <h1
              class="text-4xl md:text-5xl lg:text-6xl font-bold text-slate-900 dark:text-white mb-6 leading-tight"
            >
              {{ post.title }}
            </h1>

            <!-- Excerpt -->
            <p
              class="text-xl text-slate-600 dark:text-slate-300 mb-8 max-w-3xl mx-auto leading-relaxed"
            >
              {{ post.excerpt }}
            </p>

            <!-- Meta Information -->
            <div
              class="flex flex-col sm:flex-row items-center justify-center gap-6 text-slate-600 dark:text-slate-400 mb-8"
            >
              <div class="flex items-center">
                <div
                  class="w-12 h-12 rounded-full bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] mr-4 flex items-center justify-center text-white font-bold shadow-lg"
                >
                  {{ post.author.charAt(0) }}
                </div>
                <div class="text-left">
                  <div class="font-semibold text-slate-900 dark:text-white">
                    {{ post.author }}
                  </div>
                  <div class="text-sm">{{ post.date }}</div>
                </div>
              </div>
              <div class="flex items-center space-x-6 text-sm">
                <div class="flex items-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-4 w-4 mr-2 text-[#20D9C4]"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  {{ post.readTime }} read
                </div>
                <div class="flex items-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-4 w-4 mr-2 text-[#D6E74E]"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                    />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                    />
                  </svg>
                  {{ post.views }} views
                </div>
              </div>
            </div>

            <!-- Share Buttons -->
            <div class="flex justify-center space-x-3 mb-8">
              <button
                @click="sharePost('twitter')"
                class="p-3 rounded-xl bg-white dark:bg-slate-800 hover:bg-[#8A2BE2] hover:text-white transition-all duration-300 transform hover:scale-110 shadow-lg border border-slate-200 dark:border-slate-700"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path
                    d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"
                  />
                </svg>
              </button>
              <button
                @click="sharePost('linkedin')"
                class="p-3 rounded-xl bg-white dark:bg-slate-800 hover:bg-[#3366FF] hover:text-white transition-all duration-300 transform hover:scale-110 shadow-lg border border-slate-200 dark:border-slate-700"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path
                    d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"
                  />
                </svg>
              </button>
              <button
                @click="sharePost('facebook')"
                class="p-3 rounded-xl bg-white dark:bg-slate-800 hover:bg-[#1877F2] hover:text-white transition-all duration-300 transform hover:scale-110 shadow-lg border border-slate-200 dark:border-slate-700"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path
                    d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"
                  />
                </svg>
              </button>
              <button
                @click="copyLink"
                class="p-3 rounded-xl bg-white dark:bg-slate-800 hover:bg-[#20D9C4] hover:text-white transition-all duration-300 transform hover:scale-110 shadow-lg border border-slate-200 dark:border-slate-700"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"
                  />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- Article Layout -->
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
          <!-- Main Content -->
          <div class="lg:col-span-8">
            <!-- Featured Image -->
            <div
              class="relative rounded-3xl overflow-hidden mb-12 shadow-2xl group"
            >
              <img
                :src="post.featuredImage"
                :alt="post.title"
                class="w-full h-64 md:h-96 object-cover transform group-hover:scale-105 transition-transform duration-700"
              />
              <div
                class="absolute inset-0 bg-gradient-to-t from-black/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"
              ></div>
            </div>

            <!-- Article Content -->
            <article class="prose prose-lg dark:prose-invert max-w-none">
              <!-- Introduction -->
              <div
                class="bg-gradient-to-r from-[#8A2BE2]/5 to-[#20D9C4]/5 p-8 rounded-3xl mb-12 border border-[#8A2BE2]/10 backdrop-blur-sm"
              >
                <p
                  class="text-xl font-medium text-slate-700 dark:text-slate-300 leading-relaxed"
                >
                  {{ post.excerpt }}
                </p>
              </div>

              <!-- Main Content -->
              <div class="space-y-8">
                <div class="text-white" v-html="post.content"></div>

                <!-- Code Examples Section -->
                <section
                  class="bg-slate-50 dark:bg-slate-800/50 rounded-3xl p-8 border border-slate-200 dark:border-slate-700"
                >
                  <h2
                    class="text-3xl font-bold text-slate-900 dark:text-white mb-8 flex items-center"
                  >
                    <div
                      class="w-8 h-8 bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] rounded-lg flex items-center justify-center mr-4"
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
                    Code Examples
                  </h2>

                  <!-- JavaScript Example -->
                  <div class="mb-8">
                    <h3
                      class="text-xl font-semibold text-slate-800 dark:text-slate-200 mb-4 flex items-center"
                    >
                      <span
                        class="w-3 h-3 bg-[#D6E74E] rounded-full mr-3"
                      ></span>
                      JavaScript Implementation
                    </h3>
                    <div class="bg-slate-900 rounded-2xl p-6 overflow-x-auto">
                      <pre
                        class="text-slate-100 text-sm"
                      ><code>{{ post.codeExamples.javascript }}</code></pre>
                    </div>
                  </div>

                  <!-- Python Example -->
                  <div class="mb-8">
                    <h3
                      class="text-xl font-semibold text-slate-800 dark:text-slate-200 mb-4 flex items-center"
                    >
                      <span
                        class="w-3 h-3 bg-[#3366FF] rounded-full mr-3"
                      ></span>
                      Python Backend
                    </h3>
                    <div class="bg-slate-900 rounded-2xl p-6 overflow-x-auto">
                      <pre
                        class="text-slate-100 text-sm"
                      ><code>{{ post.codeExamples.python }}</code></pre>
                    </div>
                  </div>

                  <!-- HTML/CSS Example -->
                  <div>
                    <h3
                      class="text-xl font-semibold text-slate-800 dark:text-slate-200 mb-4 flex items-center"
                    >
                      <span
                        class="w-3 h-3 bg-[#8A2BE2] rounded-full mr-3"
                      ></span>
                      Frontend Structure
                    </h3>
                    <div class="bg-slate-900 rounded-2xl p-6 overflow-x-auto">
                      <pre
                        class="text-slate-100 text-sm"
                      ><code>{{ post.codeExamples.html }}</code></pre>
                    </div>
                  </div>
                </section>

                <!-- Folder Structure -->
                <section
                  class="bg-white dark:bg-slate-800 rounded-3xl p-8 border border-slate-200 dark:border-slate-700 shadow-lg"
                >
                  <h2
                    class="text-3xl font-bold text-slate-900 dark:text-white mb-8 flex items-center"
                  >
                    <div
                      class="w-8 h-8 bg-gradient-to-r from-[#20D9C4] to-[#D6E74E] rounded-lg flex items-center justify-center mr-4"
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
                          d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"
                        />
                      </svg>
                    </div>
                    Project Structure
                  </h2>
                  <div
                    class="bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-900 dark:to-slate-800 rounded-2xl p-6 border border-slate-200 dark:border-slate-700"
                  >
                    <div class="font-mono text-sm">
                      <FolderTree :structure="post.folderStructure" />
                    </div>
                  </div>
                </section>
              </div>
            </article>
          </div>

          <!-- Sidebar -->
          <div class="lg:col-span-4 space-y-8">
            <!-- Resources Card -->
            <div
              class="bg-gradient-to-br from-[#8A2BE2] to-[#3366FF] rounded-3xl p-8 text-white shadow-2xl"
            >
              <h3 class="text-2xl font-bold mb-6">Resources</h3>

              <!-- YouTube -->
              <div
                class="bg-white/10 rounded-2xl p-6 mb-6 backdrop-blur-sm border border-white/20"
              >
                <div class="flex items-center mb-4">
                  <div
                    class="w-12 h-12 bg-red-500 rounded-xl flex items-center justify-center mr-4 shadow-lg"
                  >
                    <svg
                      class="w-6 h-6 text-white"
                      fill="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"
                      />
                    </svg>
                  </div>
                  <div>
                    <h4 class="font-bold text-lg">Video Tutorial</h4>
                    <p class="text-white/80 text-sm">Step-by-step guide</p>
                  </div>
                </div>
                <a
                  :href="post.youtubeLink"
                  target="_blank"
                  class="w-full bg-white text-[#8A2BE2] font-semibold py-3 rounded-xl hover:bg-[#D6E74E] transition-all duration-300 transform hover:scale-105 shadow-lg flex items-center justify-center"
                >
                  Watch Tutorial
                </a>
              </div>

              <!-- GitHub -->
              <div
                class="bg-white/10 rounded-2xl p-6 backdrop-blur-sm border border-white/20"
              >
                <div class="flex items-center mb-4">
                  <div
                    class="w-12 h-12 bg-slate-800 rounded-xl flex items-center justify-center mr-4 shadow-lg"
                  >
                    <svg
                      class="w-6 h-6 text-white"
                      fill="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"
                      />
                    </svg>
                  </div>
                  <div>
                    <h4 class="font-bold text-lg">Source Code</h4>
                    <p class="text-white/80 text-sm">Complete project</p>
                  </div>
                </div>
                <a
                  :href="post.githubLink"
                  target="_blank"
                  class="w-full bg-white text-slate-800 font-semibold py-3 rounded-xl hover:bg-[#20D9C4] hover:text-white transition-all duration-300 transform hover:scale-105 shadow-lg flex items-center justify-center"
                >
                  View Repository
                </a>
              </div>
            </div>

            <!-- Services CTA -->
            <div
              class="bg-gradient-to-br from-[#20D9C4] to-[#D6E74E] rounded-3xl p-8 text-slate-900 shadow-2xl"
            >
              <h3 class="text-2xl font-bold mb-4">Need Help?</h3>
              <p class="mb-6 opacity-90">
                Let our experts bring your project to life with professional
                development services.
              </p>
              <div class="space-y-4 mb-6">
                <div class="flex items-center">
                  <div
                    class="w-8 h-8 bg-white/20 rounded-lg flex items-center justify-center mr-3"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-4 w-4"
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
                  </div>
                  <span class="font-medium">Custom Development</span>
                </div>
                <div class="flex items-center">
                  <div
                    class="w-8 h-8 bg-white/20 rounded-lg flex items-center justify-center mr-3"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-4 w-4"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
                      />
                    </svg>
                  </div>
                  <span class="font-medium">Security & Performance</span>
                </div>
              </div>
              <NuxtLink
                to="https://webdevlab.org/services"
                class="w-full bg-slate-900 text-white font-semibold py-3 rounded-xl hover:bg-[#8A2BE2] transition-all duration-300 transform hover:scale-105 shadow-lg flex items-center justify-center"
              >
                Explore Services
              </NuxtLink>
            </div>

            <!-- Tags -->
            <div
              class="bg-white dark:bg-slate-800 rounded-3xl p-8 border border-slate-200 dark:border-slate-700 shadow-lg"
            >
              <h3
                class="text-2xl font-bold text-slate-900 dark:text-white mb-6"
              >
                Tags
              </h3>
              <div class="flex flex-wrap gap-3">
                <span
                  v-for="tag in post.tags"
                  :key="tag"
                  class="px-4 py-2 bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-300 rounded-xl text-sm font-medium hover:bg-[#8A2BE2] hover:text-white transition-all duration-300 cursor-pointer"
                >
                  {{ tag }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- Related Posts -->
        <section class="mt-20">
          <div class="text-center mb-12">
            <h2 class="text-4xl font-bold text-slate-900 dark:text-white mb-4">
              Related Articles
            </h2>
            <p class="text-xl text-slate-600 dark:text-slate-400">
              Continue your learning journey
            </p>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <article
              v-for="relatedPost in relatedPosts"
              :key="relatedPost.id"
              class="bg-white dark:bg-slate-800 rounded-3xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-500 group border border-slate-200 dark:border-slate-700"
            >
              <div
                class="aspect-video bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] relative overflow-hidden"
              >
                <div
                  class="absolute inset-0 bg-black/10 group-hover:bg-black/20 transition-all duration-300"
                ></div>
              </div>
              <div class="p-6">
                <div
                  class="flex items-center text-sm text-slate-500 dark:text-slate-400 mb-3"
                >
                  <span
                    class="px-3 py-1 bg-[#8A2BE2]/10 text-[#8A2BE2] dark:text-[#20D9C4] rounded-full text-xs font-medium"
                  >
                    {{ relatedPost.category }}
                  </span>
                  <span class="mx-2">•</span>
                  <span>{{ relatedPost.readTime }}</span>
                </div>
                <h3
                  class="text-xl font-bold text-slate-900 dark:text-white mb-3 group-hover:text-[#8A2BE2] dark:group-hover:text-[#20D9C4] transition-colors duration-300"
                >
                  {{ relatedPost.title }}
                </h3>
                <p class="text-slate-600 dark:text-slate-300 mb-4 line-clamp-2">
                  {{ relatedPost.excerpt }}
                </p>
                <NuxtLink
                  :to="`/${relatedPost.slug}`"
                  class="text-[#8A2BE2] dark:text-[#20D9C4] hover:text-[#3366FF] dark:hover:text-[#D6E74E] font-medium flex items-center transition-colors duration-300 group/link"
                >
                  Read more
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
            </article>
          </div>
        </section>
      </div>
    </main>

    <!-- Footer -->
    <footer class="bg-slate-800 text-slate-300 py-12 relative z-10 mt-20">
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
// Define the post data
const post = {
  id: 1,
  title: "Building a Modern Full-Stack Application with Nuxt.js and FastAPI",
  excerpt:
    "Learn how to create a scalable full-stack application using Nuxt.js for the frontend and FastAPI for the backend with real-time features and optimized performance.",
  category: "Full Stack",
  date: "May 15, 2023",
  readTime: "15 min",
  author: "Sarah Johnson",
  slug: "modern-full-stack-nuxt-fastapi",
  views: "2.4K",
  lastUpdated: "May 18, 2023",
  featuredImage: "/images/full-stack-app.jpg",
  youtubeLink: "https://youtube.com/watch?v=example",
  githubLink: "https://github.com/webdevlab/full-stack-app",
  tags: ["Nuxt.js", "FastAPI", "Full Stack", "Python", "JavaScript", "Vue.js"],

  content: `
      <h2>Architecture Overview</h2>
      <p>In today's fast-paced development environment, building applications that are both performant and scalable is crucial. Our application follows a modern microservices architecture with a clear separation between frontend and backend concerns.</p>
      
      <p>The frontend is built with <strong>Nuxt.js</strong>, providing server-side rendering and excellent SEO capabilities, while the backend uses <strong>FastAPI</strong> for its high performance and automatic API documentation.</p>
      
      <h3>Key Features</h3>
      <ul>
        <li>Real-time updates with WebSocket connections</li>
        <li>Server-side rendering for optimal SEO</li>
        <li>Automatic API documentation with Swagger UI</li>
        <li>JWT-based authentication system</li>
        <li>File upload and processing capabilities</li>
        <li>Database integration with PostgreSQL</li>
      </ul>
      
      <h2>Setting Up the Development Environment</h2>
      <p>Before we dive into the code, let's set up our development environment. We'll be using Docker to containerize our application for consistent development and deployment across different environments.</p>
      
      <blockquote>
        <p>Pro Tip: Using Docker ensures that your development environment matches production, reducing deployment issues.</p>
      </blockquote>
      
      <h2>Frontend Implementation with Nuxt.js</h2>
      <p>Nuxt.js provides a robust framework for building Vue.js applications with built-in best practices. We'll leverage its file-based routing, auto-imports, and server-side rendering capabilities.</p>
    `,

  codeExamples: {
    javascript: `// Nuxt.js configuration
  export default defineNuxtConfig({
    ssr: true,
    modules: [
      '@nuxtjs/tailwindcss',
      '@pinia/nuxt',
    ],
    runtimeConfig: {
      public: {
        apiBase: process.env.API_BASE_URL || 'http://localhost:8000'
      }
    },
    css: ['~/assets/css/main.css'],
    build: {
      transpile: ['@headlessui/vue']
    }
  })
  
  // API integration with composables
  export const useApi = () => {
    const config = useRuntimeConfig()
    
    const fetchData = async (endpoint) => {
      const { data, error } = await useFetch(\`\${config.public.apiBase}\${endpoint}\`)
      
      if (error.value) {
        throw createError({
          statusCode: error.value.statusCode,
          statusMessage: error.value.statusMessage
        })
      }
      
      return data.value
    }
    
    return { fetchData }
  }`,

    python: `# FastAPI main application
  from fastapi import FastAPI, Depends, HTTPException
  from fastapi.middleware.cors import CORSMiddleware
  from sqlalchemy.orm import Session
  from typing import List
  
  from . import models, schemas, crud
  from .database import SessionLocal, engine
  
  models.Base.metadata.create_all(bind=engine)
  
  app = FastAPI(
      title="Full Stack API",
      description="Backend API for our full-stack application",
      version="1.0.0"
  )
  
  # CORS middleware
  app.add_middleware(
      CORSMiddleware,
      allow_origins=["http://localhost:3000"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )
  
  # Dependency
  def get_db():
      db = SessionLocal()
      try:
          yield db
      finally:
          db.close()
  
  @app.get("/")
  async def root():
      return {"message": "Welcome to Full Stack API"}
  
  @app.get("/items/", response_model=List[schemas.Item])
  def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
      items = crud.get_items(db, skip=skip, limit=limit)
      return items`,

    html: `<!-- Nuxt.js layout component -->
  <template>
    <div class="min-h-screen bg-gray-50">
      <header class="bg-white shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="flex justify-between items-center py-4">
            <div class="flex items-center">
              <NuxtLink to="/" class="text-xl font-bold text-indigo-600">
                FullStackApp
              </NuxtLink>
            </div>
            <nav class="hidden md:flex space-x-8">
              <NuxtLink 
                to="/" 
                class="text-gray-600 hover:text-indigo-600 transition-colors"
              >
                Home
              </NuxtLink>
              <NuxtLink 
                to="/dashboard" 
                class="text-gray-600 hover:text-indigo-600 transition-colors"
              >
                Dashboard
              </NuxtLink>
            </nav>
          </div>
        </div>
      </header>
      
      <main>
        <slot />
      </main>
    </div>
  </template>
  
  <style scoped>
  .router-link-active {
    @apply text-indigo-600 font-medium;
  }
  </style>`,
  },

  folderStructure: {
    name: "full-stack-app",
    type: "folder",
    children: [
      {
        name: "frontend",
        type: "folder",
        children: [
          { name: "components", type: "folder" },
          { name: "pages", type: "folder" },
          { name: "layouts", type: "folder" },
          { name: "assets", type: "folder" },
          { name: "nuxt.config.ts", type: "file" },
          { name: "package.json", type: "file" },
        ],
      },
      {
        name: "backend",
        type: "folder",
        children: [
          { name: "app", type: "folder" },
          { name: "models", type: "folder" },
          { name: "schemas", type: "folder" },
          { name: "crud", type: "folder" },
          { name: "main.py", type: "file" },
          { name: "requirements.txt", type: "file" },
        ],
      },
      {
        name: "docker-compose.yml",
        type: "file",
      },
      {
        name: "README.md",
        type: "file",
      },
    ],
  },

  gallery: [
    {
      src: "/images/architecture-diagram.jpg",
      alt: "Application Architecture Diagram",
      caption: "System Architecture Overview",
    },
    {
      src: "/images/api-docs.jpg",
      alt: "API Documentation",
      caption: "Auto-generated API Documentation",
    },
    {
      src: "/images/frontend-demo.jpg",
      alt: "Frontend Demo",
      caption: "Frontend Application Interface",
    },
    {
      src: "/images/database-schema.jpg",
      alt: "Database Schema",
      caption: "Database Structure Design",
    },
  ],
};

// Related posts
const relatedPosts = [
  {
    id: 2,
    title: "Advanced State Management with Pinia in Nuxt.js",
    excerpt:
      "Learn how to implement scalable state management in your Nuxt.js applications using Pinia.",
    category: "Frontend",
    readTime: "8 min",
    slug: "advanced-state-management-pinia-nuxt",
  },
  {
    id: 3,
    title: "Building RESTful APIs with FastAPI and SQLAlchemy",
    excerpt:
      "Create high-performance REST APIs with automatic documentation using FastAPI and SQLAlchemy ORM.",
    category: "Backend",
    readTime: "12 min",
    slug: "restful-apis-fastapi-sqlalchemy",
  },
  {
    id: 4,
    title: "Deploying Full-Stack Applications with Docker and CI/CD",
    excerpt:
      "Complete guide to containerizing and deploying your applications with automated pipelines.",
    category: "DevOps",
    readTime: "10 min",
    slug: "deploying-docker-ci-cd",
  },
];

// Reactive state
const darkMode = ref(false);
const showCopied = ref(false);

// Methods
function toggleTheme() {
  darkMode.value = !darkMode.value;
  if (darkMode.value) {
    document.documentElement.classList.add("dark");
  } else {
    document.documentElement.classList.remove("dark");
  }
}

function sharePost(platform) {
  const url = window.location.href;
  const title = post.title;

  const shareUrls = {
    twitter: `https://twitter.com/intent/tweet?text=${encodeURIComponent(
      title
    )}&url=${encodeURIComponent(url)}`,
    linkedin: `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(
      url
    )}`,
    facebook: `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(
      url
    )}`,
  };

  window.open(shareUrls[platform], "_blank", "width=600,height=400");
}

async function copyLink() {
  const url = window.location.href;
  try {
    await navigator.clipboard.writeText(url);
    showCopied.value = true;
    setTimeout(() => (showCopied.value = false), 2000);
  } catch (err) {
    console.error("Failed to copy: ", err);
  }
}

// Set page metadata
useHead({
  title: `${post.title} - WebDevLab`,
  meta: [
    {
      name: "description",
      content: post.excerpt,
    },
    {
      property: "og:title",
      content: post.title,
    },
    {
      property: "og:description",
      content: post.excerpt,
    },
    {
      property: "og:type",
      content: "article",
    },
    {
      name: "twitter:card",
      content: "summary_large_image",
    },
  ],
});
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
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

.animate-float-slow {
  animation: float-slow 10s ease-in-out infinite;
}

.animate-float-medium {
  animation: float-medium 8s ease-in-out infinite;
}

.animate-float-fast {
  animation: float-fast 6s ease-in-out infinite;
}

/* Custom prose styles for better readability */
.prose {
  max-width: none;
}

.prose h2 {
  @apply text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4;
}

.prose h3 {
  @apply text-xl font-semibold text-slate-800 dark:text-slate-200 mt-6 mb-3;
}

.prose p {
  @apply text-slate-700 dark:text-slate-300 leading-relaxed mb-4;
}

.prose ul {
  @apply text-slate-700 dark:text-slate-300 mb-4;
}

.prose li {
  @apply mb-2;
}

.prose blockquote {
  @apply border-l-4 border-[#8A2BE2] bg-[#8A2BE2]/5 dark:bg-[#8A2BE2]/10 pl-6 py-4 my-6 rounded-r-xl;
}

.prose blockquote p {
  @apply text-slate-700 dark:text-slate-300 italic mb-0;
}
</style>
