<template>
    <div
      class="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-900 dark:to-slate-800 transition-all duration-500"
    >
      <!-- Animated Background Elements -->
      <div class="fixed inset-0 overflow-hidden pointer-events-none z-0">
        <div
          class="absolute -top-40 -right-40 w-80 h-80 bg-[#8A2BE2]/5 rounded-full mix-blend-multiply dark:mix-blend-screen filter blur-3xl animate-float-slow"
        ></div>
        <div
          class="absolute -bottom-40 -left-40 w-80 h-80 bg-[#20D9C4]/5 rounded-full mix-blend-multiply dark:mix-blend-screen filter blur-3xl animate-float-medium"
          style="animation-delay: 2s"
        ></div>
        <div
          class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-[#D6E74E]/5 rounded-full mix-blend-multiply dark:mix-blend-screen filter blur-3xl animate-float-fast"
          style="animation-delay: 4s"
        ></div>
  
        <!-- Subtle Grid Pattern -->
        <div class="absolute inset-0 opacity-3">
          <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <pattern
                id="adminGrid"
                width="40"
                height="40"
                patternUnits="userSpaceOnUse"
              >
                <path
                  d="M 40 0 L 0 0 0 40"
                  fill="none"
                  stroke="#8A2BE2"
                  stroke-width="0.5"
                  opacity="0.1"
                />
              </pattern>
            </defs>
            <rect width="100%" height="100%" fill="url(#adminGrid)" />
          </svg>
        </div>
      </div>
  
      <div class="flex h-screen">
        <!-- Desktop Sidebar -->
        <aside
          class="hidden md:flex md:w-64 lg:w-72 h-full bg-white/80 dark:bg-slate-900/80 backdrop-blur-md border-r border-slate-200/50 dark:border-slate-700/50 overflow-y-auto"
        >
          <div class="flex flex-col h-full py-6">
            <div class="px-4 mb-8">
              <NuxtLink to="/" class="flex items-center space-x-2 group">
                <NuxtImg
                  src="/images/logo-light.png"
                  class="w-10 h-10 rounded-lg"
                />
                <span
                  class="text-xl font-bold text-slate-900 dark:text-white"
                >
                  Admin
                </span>
              </NuxtLink>
            </div>
            <nav class="flex-1 px-4 space-y-2">
              <a
                v-for="item in navItems"
                :key="item.name"
                :href="item.href"
                @click="setActiveTab(item.name)"
                :class="[
                  'flex items-center px-4 py-3 rounded-xl text-sm font-medium transition-all duration-300 group',
                  activeTab === item.name
                    ? 'bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] text-white shadow-lg'
                    : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-[#8A2BE2] dark:hover:text-[#20D9C4]'
                ]"
              >
                <span class="w-6 h-6 mr-3 flex items-center justify-center">
                  <component :is="item.icon" class="w-5 h-5" />
                </span>
                {{ item.name }}
                <span
                  v-if="activeTab === item.name"
                  class="ml-auto w-2 h-2 bg-white rounded-full animate-pulse"
                ></span>
              </a>
            </nav>
          </div>
        </aside>
  
        <!-- Mobile Sidebar Overlay -->
        <aside
          :class="[
            'md:hidden fixed inset-y-0 left-0 z-50 w-64 lg:w-72 bg-white/80 dark:bg-slate-900/80 backdrop-blur-md border-r border-slate-200/50 dark:border-slate-700/50 transform -translate-x-full transition-transform duration-300 ease-in-out overflow-y-auto',
            sidebarOpen ? 'translate-x-0' : ''
          ]"
        >
          <div class="flex flex-col h-full py-6">
            <div class="px-4 mb-8">
              <div class="flex items-center justify-between">
                <NuxtLink to="/" class="flex items-center space-x-2 group">
                  <NuxtImg
                    src="/images/logo-light.png"
                    class="w-10 h-10 rounded-lg"
                  />
                  <span class="text-xl font-bold text-slate-900 dark:text-white">
                    Admin
                  </span>
                </NuxtLink>
                <button
                  @click="toggleSidebar"
                  class="p-2 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all duration-300"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                </button>
              </div>
            </div>
            <nav class="flex-1 px-4 space-y-2">
              <a
                v-for="item in navItems"
                :key="item.name"
                :href="item.href"
                @click="setActiveTab(item.name)"
                :class="[
                  'flex items-center px-4 py-3 rounded-xl text-sm font-medium transition-all duration-300 group',
                  activeTab === item.name
                    ? 'bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] text-white shadow-lg'
                    : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-[#8A2BE2] dark:hover:text-[#20D9C4]'
                ]"
              >
                <span class="w-6 h-6 mr-3 flex items-center justify-center">
                  <component :is="item.icon" class="w-5 h-5" />
                </span>
                {{ item.name }}
                <span
                  v-if="activeTab === item.name"
                  class="ml-auto w-2 h-2 bg-white rounded-full animate-pulse"
                ></span>
              </a>
            </nav>
          </div>
        </aside>
  
        <!-- Overlay for mobile sidebar -->
        <div
          v-if="sidebarOpen"
          @click="toggleSidebar"
          class="fixed inset-0 bg-black/50 md:hidden z-40 transition-opacity duration-300"
        ></div>
  
        <!-- Main Content Area -->
        <div class="flex-1 flex flex-col overflow-hidden">
          <!-- Header -->
          <header
            class="sticky top-0 z-40 backdrop-blur-md bg-white/90 dark:bg-slate-900/90 border-b border-slate-200/50 dark:border-slate-700/50 transition-all duration-500 flex-shrink-0"
          >
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
              <div class="flex justify-between items-center py-4">
                <div class="flex items-center space-x-4">
                  <button
                    @click="toggleSidebar"
                    class="md:hidden p-2 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-all duration-300"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-6 w-6"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M4 6h16M4 12h16M4 18h16"
                      />
                    </svg>
                  </button>
                  <span
                    class="text-xl font-bold text-slate-900 dark:text-white hidden md:block"
                  >
                    Admin Panel
                  </span>
                </div>
  
                <!-- Actions -->
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
                    class="px-4 py-2 bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] text-white font-medium rounded-lg hover:from-[#7A1BD2] hover:to-[#2A56EF] transition-all duration-300 transform hover:scale-105 shadow-lg"
                  >
                    Logout
                  </button>
                </div>
              </div>
            </div>
          </header>
  
          <!-- Scrollable Main Content -->
          <main class="flex-1 overflow-y-auto p-4 md:p-8 relative z-10">
            <!-- Breadcrumb -->
            <nav class="flex mb-6 text-sm text-slate-500 dark:text-slate-400 animate-fade-in-up">
              <a href="#" class="hover:text-[#8A2BE2] dark:hover:text-[#20D9C4] transition-colors duration-300 flex items-center">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2H5a2 2 0 00-2 2z" />
                </svg>
                Dashboard
              </a>
              <span class="mx-2">/</span>
              <span class="font-medium text-slate-700 dark:text-slate-300">{{ activeTab }}</span>
            </nav>
  
            <!-- Tab Content -->
            <div class="space-y-8">
              <!-- Dashboard Tab -->
              <div v-if="activeTab === 'Dashboard'" class="animate-fade-in-up">
                <h1 class="text-3xl font-bold text-slate-900 dark:text-white mb-6">Admin Dashboard</h1>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                  <div
                    class="bg-white dark:bg-slate-800 rounded-2xl p-6 border border-slate-200/50 dark:border-slate-700/50 shadow-sm hover:shadow-md transition-all duration-300 transform hover:scale-105 group"
                  >
                    <div class="flex items-center justify-between mb-4">
                      <div class="p-3 bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] rounded-xl text-white">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                        </svg>
                      </div>
                      <span class="text-2xl font-bold text-[#8A2BE2] dark:text-[#20D9C4] group-hover:scale-110 transition-transform duration-300">{{ stats.totalPosts }}</span>
                    </div>
                    <p class="text-slate-600 dark:text-slate-300 text-sm">Total Posts</p>
                  </div>
                  <div
                    class="bg-white dark:bg-slate-800 rounded-2xl p-6 border border-slate-200/50 dark:border-slate-700/50 shadow-sm hover:shadow-md transition-all duration-300 transform hover:scale-105 group"
                  >
                    <div class="flex items-center justify-between mb-4">
                      <div class="p-3 bg-gradient-to-r from-[#20D9C4] to-[#3366FF] rounded-xl text-white">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z" />
                        </svg>
                      </div>
                      <span class="text-2xl font-bold text-[#20D9C4] dark:text-[#D6E74E] group-hover:scale-110 transition-transform duration-300">{{ stats.totalUsers }}</span>
                    </div>
                    <p class="text-slate-600 dark:text-slate-300 text-sm">Total Users</p>
                  </div>
                  <div
                    class="bg-white dark:bg-slate-800 rounded-2xl p-6 border border-slate-200/50 dark:border-slate-700/50 shadow-sm hover:shadow-md transition-all duration-300 transform hover:scale-105 group"
                  >
                    <div class="flex items-center justify-between mb-4">
                      <div class="p-3 bg-gradient-to-r from-[#D6E74E] to-[#20D9C4] rounded-xl text-white">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z" />
                        </svg>
                      </div>
                      <span class="text-2xl font-bold text-[#D6E74E] dark:text-[#8A2BE2] group-hover:scale-110 transition-transform duration-300">{{ stats.totalCategories }}</span>
                    </div>
                    <p class="text-slate-600 dark:text-slate-300 text-sm">Categories</p>
                  </div>
                  <div
                    class="bg-white dark:bg-slate-800 rounded-2xl p-6 border border-slate-200/50 dark:border-slate-700/50 shadow-sm hover:shadow-md transition-all duration-300 transform hover:scale-105 group"
                  >
                    <div class="flex items-center justify-between mb-4">
                      <div class="p-3 bg-gradient-to-r from-[#3366FF] to-[#8A2BE2] rounded-xl text-white">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                        </svg>
                      </div>
                      <span class="text-2xl font-bold text-[#3366FF] dark:text-[#20D9C4] group-hover:scale-110 transition-transform duration-300">{{ stats.views }}</span>
                    </div>
                    <p class="text-slate-600 dark:text-slate-300 text-sm">Total Views</p>
                  </div>
                </div>
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                  <div class="bg-white dark:bg-slate-800 rounded-2xl p-6 border border-slate-200/50 dark:border-slate-700/50">
                    <h3 class="text-lg font-semibold text-slate-900 dark:text-white mb-4">Recent Activity</h3>
                    <ul class="space-y-3">
                      <li v-for="(activity, index) in recentActivities" :key="index" class="flex items-center text-sm text-slate-600 dark:text-slate-300 animate-fade-in-up" :style="`animation-delay: ${index * 0.1}s`">
                        <div class="w-2 h-2 bg-[#8A2BE2] rounded-full mr-3"></div>
                        {{ activity }}
                      </li>
                    </ul>
                  </div>
                  <div class="bg-white dark:bg-slate-800 rounded-2xl p-6 border border-slate-200/50 dark:border-slate-700/50">
                    <h3 class="text-lg font-semibold text-slate-900 dark:text-white mb-4">Quick Actions</h3>
                    <div class="space-y-3">
                      <button @click="setActiveTab('Posts'); startEditPost(null)" class="w-full bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] text-white py-3 rounded-lg hover:from-[#7A1BD2] hover:to-[#2A56EF] transition-all duration-300 transform hover:scale-105">
                        Add New Post
                      </button>
                      <button @click="setActiveTab('Users'); startEditUser(null)" class="w-full bg-gradient-to-r from-[#20D9C4] to-[#D6E74E] text-white py-3 rounded-lg hover:from-[#0EB8A8] hover:to-[#B8C93A] transition-all duration-300 transform hover:scale-105">
                        Manage Users
                      </button>
                    </div>
                  </div>
                </div>
              </div>
  
              <!-- Posts Tab -->
              <div v-if="activeTab === 'Posts'" class="animate-fade-in-up">
                <div v-if="!editingPostId" class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6 gap-4">
                  <div>
                    <h1 class="text-3xl font-bold text-slate-900 dark:text-white">Manage Posts</h1>
                    <p class="text-slate-600 dark:text-slate-400">Create, edit, and delete blog posts</p>
                  </div>
                  <button
                    @click="startEditPost(null)"
                    class="bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] text-white font-medium px-6 py-3 rounded-lg hover:from-[#7A1BD2] hover:to-[#2A56EF] transition-all duration-300 transform hover:scale-105 shadow-lg"
                  >
                    Add New Post
                  </button>
                </div>
  
                <!-- Posts List View -->
                <div v-if="!editingPostId" class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200/50 dark:border-slate-700/50 overflow-hidden shadow-sm">
                  <div class="overflow-x-auto">
                    <table class="w-full min-w-[600px]">
                      <thead class="bg-slate-50 dark:bg-slate-700">
                        <tr>
                          <th class="px-6 py-4 text-left text-xs font-medium text-slate-500 dark:text-slate-400 uppercase tracking-wider">Title</th>
                          <th class="px-6 py-4 text-left text-xs font-medium text-slate-500 dark:text-slate-400 uppercase tracking-wider">Category</th>
                          <th class="px-6 py-4 text-left text-xs font-medium text-slate-500 dark:text-slate-400 uppercase tracking-wider">Author</th>
                          <th class="px-6 py-4 text-left text-xs font-medium text-slate-500 dark:text-slate-400 uppercase tracking-wider">Date</th>
                          <th class="px-6 py-4 text-right text-xs font-medium text-slate-500 dark:text-slate-400 uppercase tracking-wider">Actions</th>
                        </tr>
                      </thead>
                      <tbody class="divide-y divide-slate-200 dark:divide-slate-700">
                        <tr v-for="post in posts" :key="post.id" class="hover:bg-slate-50 dark:hover:bg-slate-700 transition-colors duration-200">
                          <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900 dark:text-white line-clamp-1 max-w-xs">{{ post.title }}</td>
                          <td class="px-6 py-4 whitespace-nowrap">
                            <span class="px-3 py-1 bg-gradient-to-r from-[#8A2BE2]/10 to-[#3366FF]/10 text-[#8A2BE2] dark:text-[#20D9C4] text-xs font-medium rounded-full">
                              {{ post.category }}
                            </span>
                          </td>
                          <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-500 dark:text-slate-400">{{ post.author }}</td>
                          <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-500 dark:text-slate-400">{{ post.date }}</td>
                          <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium space-x-2">
                            <button
                              @click="startEditPost(post)"
                              class="text-[#20D9C4] hover:text-[#0EB8A8] transition-colors duration-300"
                            >
                              Edit
                            </button>
                            <button
                              @click="deletePost(post.id)"
                              class="text-red-500 hover:text-red-700 transition-colors duration-300"
                            >
                              Delete
                            </button>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
  
                <!-- Posts Edit View -->
                <div v-if="editingPostId" class="animate-fade-in-up">
                  <div class="flex items-center mb-6">
                    <button @click="cancelEditPost" class="flex items-center text-slate-600 dark:text-slate-300 hover:text-[#8A2BE2] dark:hover:text-[#20D9C4] transition-colors duration-300 mr-4">
                      <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                      </svg>
                      Back to Posts
                    </button>
                    <h1 class="text-3xl font-bold text-slate-900 dark:text-white">{{ editingPost ? 'Edit Post' : 'Add New Post' }}</h1>
                  </div>
                  <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200/50 dark:border-slate-700/50 p-6 md:p-8 shadow-sm">
                    <form @submit.prevent="savePost" class="space-y-6 max-w-2xl">
                      <div>
                        <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">Title</label>
                        <input
                          v-model="form.title"
                          type="text"
                          class="w-full px-4 py-3 rounded-lg border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-[#8A2BE2] bg-white dark:bg-slate-900 text-slate-900 dark:text-white transition-all duration-300"
                          required
                        />
                      </div>
                      <div>
                        <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">Excerpt</label>
                        <textarea
                          v-model="form.excerpt"
                          rows="4"
                          class="w-full px-4 py-3 rounded-lg border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-[#8A2BE2] bg-white dark:bg-slate-900 text-slate-900 dark:text-white transition-all duration-300"
                          required
                        ></textarea>
                      </div>
                      <div>
                        <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">Category</label>
                        <select
                          v-model="form.category"
                          class="w-full px-4 py-3 rounded-lg border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-[#8A2BE2] bg-white dark:bg-slate-900 text-slate-900 dark:text-white transition-all duration-300"
                          required
                        >
                          <option v-for="cat in categories.filter(c => c !== 'All')" :key="cat" :value="cat">{{ cat }}</option>
                        </select>
                      </div>
                      <div>
                        <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">Author</label>
                        <input
                          v-model="form.author"
                          type="text"
                          class="w-full px-4 py-3 rounded-lg border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-[#8A2BE2] bg-white dark:bg-slate-900 text-slate-900 dark:text-white transition-all duration-300"
                          required
                        />
                      </div>
                      <div class="flex justify-end space-x-3 pt-4">
                        <button
                          type="button"
                          @click="cancelEditPost"
                          class="px-6 py-3 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 transition-all duration-300"
                        >
                          Cancel
                        </button>
                        <button
                          type="submit"
                          class="bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] text-white px-6 py-3 rounded-lg hover:from-[#7A1BD2] hover:to-[#2A56EF] transition-all duration-300 transform hover:scale-105 shadow-lg"
                        >
                          Save Post
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
  
              <!-- Categories Tab -->
              <div v-if="activeTab === 'Categories'" class="animate-fade-in-up">
                <div v-if="!editingCategory" class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6 gap-4">
                  <div>
                    <h1 class="text-3xl font-bold text-slate-900 dark:text-white">Manage Categories</h1>
                    <p class="text-slate-600 dark:text-slate-400">Add and remove post categories</p>
                  </div>
                  <button
                    @click="startEditCategory(null)"
                    class="bg-gradient-to-r from-[#D6E74E] to-[#20D9C4] text-slate-900 font-medium px-6 py-3 rounded-lg hover:from-[#B8C93A] hover:to-[#0EB8A8] transition-all duration-300 transform hover:scale-105 shadow-lg"
                  >
                    Add Category
                  </button>
                </div>
  
                <!-- Categories List View -->
                <div v-if="!editingCategory" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                  <div
                    v-for="category in categories.filter(c => c !== 'All')"
                    :key="category"
                    class="bg-white dark:bg-slate-800 rounded-xl p-4 border border-slate-200/50 dark:border-slate-700/50 shadow-sm hover:shadow-md transition-all duration-300 group flex items-center justify-between cursor-pointer"
                    @click="startEditCategory(category)"
                  >
                    <span class="text-lg font-medium text-slate-900 dark:text-white flex items-center">
                      <span v-if="category === 'AI'" class="mr-2">🤖</span>
                      <span v-if="category === 'Web3'" class="mr-2">⛓️</span>
                      <span v-if="category === 'Mobile'" class="mr-2">📱</span>
                      <span v-if="category === 'Backend'" class="mr-2">⚙️</span>
                      <span v-if="category === 'Full Stack'" class="mr-2">🔄</span>
                      {{ category }}
                    </span>
                    <button
                      @click.stop="deleteCategory(category)"
                      class="text-red-500 hover:text-red-700 transition-colors duration-300 opacity-0 group-hover:opacity-100 ml-2"
                    >
                      ×
                    </button>
                  </div>
                </div>
  
                <!-- Categories Edit View -->
                <div v-if="editingCategory" class="animate-fade-in-up">
                  <div class="flex items-center mb-6">
                    <button @click="cancelEditCategory" class="flex items-center text-slate-600 dark:text-slate-300 hover:text-[#D6E74E] dark:hover:text-[#20D9C4] transition-colors duration-300 mr-4">
                      <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                      </svg>
                      Back to Categories
                    </button>
                    <h1 class="text-3xl font-bold text-slate-900 dark:text-white">{{ editingCategoryName ? 'Edit Category' : 'Add New Category' }}</h1>
                  </div>
                  <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200/50 dark:border-slate-700/50 p-6 md:p-8 shadow-sm max-w-md">
                    <form @submit.prevent="saveCategory" class="space-y-6">
                      <div>
                        <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">Category Name</label>
                        <input
                          v-model="categoryForm.name"
                          type="text"
                          class="w-full px-4 py-3 rounded-lg border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-[#D6E74E] bg-white dark:bg-slate-900 text-slate-900 dark:text-white transition-all duration-300"
                          required
                        />
                      </div>
                      <div class="flex justify-end space-x-3 pt-4">
                        <button
                          type="button"
                          @click="cancelEditCategory"
                          class="px-6 py-3 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 transition-all duration-300"
                        >
                          Cancel
                        </button>
                        <button
                          type="submit"
                          class="bg-gradient-to-r from-[#D6E74E] to-[#20D9C4] text-slate-900 px-6 py-3 rounded-lg hover:from-[#B8C93A] hover:to-[#0EB8A8] transition-all duration-300 transform hover:scale-105 shadow-lg"
                        >
                          Save Category
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
  
              <!-- Users Tab -->
              <div v-if="activeTab === 'Users'" class="animate-fade-in-up">
                <div v-if="!editingUserId" class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6 gap-4">
                  <div>
                    <h1 class="text-3xl font-bold text-slate-900 dark:text-white">Manage Users</h1>
                    <p class="text-slate-600 dark:text-slate-400">View and add staff members</p>
                  </div>
                  <button
                    @click="startEditUser(null)"
                    class="bg-gradient-to-r from-[#3366FF] to-[#8A2BE2] text-white font-medium px-6 py-3 rounded-lg hover:from-[#2A56EF] hover:to-[#7A1BD2] transition-all duration-300 transform hover:scale-105 shadow-lg"
                  >
                    Add User
                  </button>
                </div>
  
                <!-- Users List View -->
                <div v-if="!editingUserId" class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200/50 dark:border-slate-700/50 overflow-hidden shadow-sm">
                  <div class="overflow-x-auto">
                    <table class="w-full min-w-[500px]">
                      <thead class="bg-slate-50 dark:bg-slate-700">
                        <tr>
                          <th class="px-6 py-4 text-left text-xs font-medium text-slate-500 dark:text-slate-400 uppercase tracking-wider">Name</th>
                          <th class="px-6 py-4 text-left text-xs font-medium text-slate-500 dark:text-slate-400 uppercase tracking-wider">Email</th>
                          <th class="px-6 py-4 text-left text-xs font-medium text-slate-500 dark:text-slate-400 uppercase tracking-wider">Role</th>
                          <th class="px-6 py-4 text-right text-xs font-medium text-slate-500 dark:text-slate-400 uppercase tracking-wider">Actions</th>
                        </tr>
                      </thead>
                      <tbody class="divide-y divide-slate-200 dark:divide-slate-700">
                        <tr v-for="user in users" :key="user.id" class="hover:bg-slate-50 dark:hover:bg-slate-700 transition-colors duration-200">
                          <td class="px-6 py-4 whitespace-nowrap">
                            <div class="flex items-center">
                              <div class="w-10 h-10 bg-gradient-to-r from-[#8A2BE2] to-[#3366FF] rounded-full flex items-center justify-center text-white font-bold mr-3">
                                {{ user.name.charAt(0) }}
                              </div>
                              <span class="text-sm font-medium text-slate-900 dark:text-white">{{ user.name }}</span>
                            </div>
                          </td>
                          <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-500 dark:text-slate-400">{{ user.email }}</td>
                          <td class="px-6 py-4 whitespace-nowrap">
                            <span class="px-2 py-1 bg-[#20D9C4]/10 text-[#20D9C4] text-xs font-medium rounded-full">{{ user.role }}</span>
                          </td>
                          <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium space-x-2">
                            <button
                              @click="startEditUser(user)"
                              class="text-[#20D9C4] hover:text-[#0EB8A8] transition-colors duration-300"
                            >
                              Edit
                            </button>
                            <button
                              @click="deleteUser(user.id)"
                              class="text-red-500 hover:text-red-700 transition-colors duration-300"
                            >
                              Delete
                            </button>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
  
                <!-- Users Edit View -->
                <div v-if="editingUserId" class="animate-fade-in-up">
                  <div class="flex items-center mb-6">
                    <button @click="cancelEditUser" class="flex items-center text-slate-600 dark:text-slate-300 hover:text-[#3366FF] dark:hover:text-[#8A2BE2] transition-colors duration-300 mr-4">
                      <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                      </svg>
                      Back to Users
                    </button>
                    <h1 class="text-3xl font-bold text-slate-900 dark:text-white">{{ editingUser ? 'Edit User' : 'Add New User' }}</h1>
                  </div>
                  <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200/50 dark:border-slate-700/50 p-6 md:p-8 shadow-sm max-w-2xl">
                    <form @submit.prevent="saveUser" class="space-y-6">
                      <div>
                        <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">Name</label>
                        <input
                          v-model="userForm.name"
                          type="text"
                          class="w-full px-4 py-3 rounded-lg border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-[#3366FF] bg-white dark:bg-slate-900 text-slate-900 dark:text-white transition-all duration-300"
                          required
                        />
                      </div>
                      <div>
                        <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">Email</label>
                        <input
                          v-model="userForm.email"
                          type="email"
                          class="w-full px-4 py-3 rounded-lg border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-[#3366FF] bg-white dark:bg-slate-900 text-slate-900 dark:text-white transition-all duration-300"
                          required
                        />
                      </div>
                      <div>
                        <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">Role</label>
                        <select
                          v-model="userForm.role"
                          class="w-full px-4 py-3 rounded-lg border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-[#3366FF] bg-white dark:bg-slate-900 text-slate-900 dark:text-white transition-all duration-300"
                          required
                        >
                          <option value="Admin">Admin</option>
                          <option value="Editor">Editor</option>
                          <option value="Author">Author</option>
                        </select>
                      </div>
                      <div class="flex justify-end space-x-3 pt-4">
                        <button
                          type="button"
                          @click="cancelEditUser"
                          class="px-6 py-3 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 transition-all duration-300"
                        >
                          Cancel
                        </button>
                        <button
                          type="submit"
                          class="bg-gradient-to-r from-[#3366FF] to-[#8A2BE2] text-white px-6 py-3 rounded-lg hover:from-[#2A56EF] hover:to-[#7A1BD2] transition-all duration-300 transform hover:scale-105 shadow-lg"
                        >
                          Save User
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </main>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  // Imports for icons (assuming Heroicons or similar)
  const HomeIcon = { template: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" /></svg>' };
  const PostIcon = { template: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg>' };
  const CategoryIcon = { template: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" /></svg>' };
  const UserIcon = { template: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z" /></svg>' };
  
  // Navigation items
  const navItems = [
    { name: 'Dashboard', href: '#', icon: HomeIcon },
    { name: 'Posts', href: '#', icon: PostIcon },
    { name: 'Categories', href: '#', icon: CategoryIcon },
    { name: 'Users', href: '#', icon: UserIcon },
  ];
  
  // Reactive state
  const sidebarOpen = ref(false);
  const activeTab = ref('Dashboard');
  const darkMode = ref(false);
  const editingPostId = ref(null);
  const editingPost = ref(null);
  const editingUserId = ref(null);
  const editingUser = ref(null);
  const editingCategory = ref(null);
  const editingCategoryName = ref('');
  
  // Mock data
  const posts = ref([
    {
      id: 1,
      title: "Understanding Web3: The Decentralized Future",
      excerpt: "Explore Web3 transformations...",
      category: "Web3",
      author: "Sarah Johnson",
      date: "May 15, 2023",
    },
    {
      id: 2,
      title: "AI-Powered Development",
      excerpt: "Discover AI in software dev...",
      category: "AI",
      author: "Michael Chen",
      date: "April 28, 2023",
    },
  ]);
  
  const categories = ref(["All", "Web3", "AI", "Mobile", "Backend", "Full Stack"]);
  
  const users = ref([
    { id: 1, name: "Admin User", email: "admin@webdevlab.com", role: "Admin" },
    { id: 2, name: "Sarah Johnson", email: "sarah@webdevlab.com", role: "Editor" },
    { id: 3, name: "Michael Chen", email: "michael@webdevlab.com", role: "Author" },
  ]);
  
  const stats = ref({
    totalPosts: 6,
    totalUsers: 3,
    totalCategories: 5,
    views: 12456,
  });
  
  const recentActivities = ref([
    "New post published: AI-Powered Development",
    "User Sarah Johnson promoted to Editor",
    "Category 'Web3' updated",
    "5 new comments approved",
  ]);
  
  // Form data
  const form = ref({
    title: '',
    excerpt: '',
    category: '',
    author: '',
  });
  
  const userForm = ref({
    name: '',
    email: '',
    role: 'Author',
  });
  
  const categoryForm = ref({
    name: '',
  });
  
  // Functions
  function toggleSidebar() {
    sidebarOpen.value = !sidebarOpen.value;
  }
  
  function setActiveTab(tab) {
    activeTab.value = tab;
    if (sidebarOpen.value) sidebarOpen.value = false;
    // Reset editing states when switching tabs
    editingPostId.value = null;
    editingPost.value = null;
    editingUserId.value = null;
    editingUser.value = null;
    editingCategory.value = null;
    editingCategoryName.value = '';
  }
  
  function toggleTheme() {
    darkMode.value = !darkMode.value;
    if (darkMode.value) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }
  
  // Post functions
  function startEditPost(post) {
    editingPostId.value = post ? post.id : 'new';
    editingPost.value = post;
    form.value = post ? { ...post } : { title: '', excerpt: '', category: '', author: '' };
  }
  
  function cancelEditPost() {
    editingPostId.value = null;
    editingPost.value = null;
    form.value = { title: '', excerpt: '', category: '', author: '' };
  }
  
  function savePost() {
    if (editingPost.value) {
      const index = posts.value.findIndex(p => p.id === editingPost.value.id);
      posts.value[index] = { ...form.value, id: editingPost.value.id, date: editingPost.value.date };
    } else {
      const newPost = { ...form.value, id: Date.now(), date: new Date().toLocaleDateString() };
      posts.value.unshift(newPost);
      stats.value.totalPosts++;
    }
    cancelEditPost();
  }
  
  function deletePost(id) {
    if (confirm('Delete this post?')) {
      posts.value = posts.value.filter(p => p.id !== id);
      stats.value.totalPosts--;
    }
  }
  
  // Category functions
  function startEditCategory(category) {
    editingCategory.value = category || 'new';
    editingCategoryName.value = category ? `Edit ${category}` : '';
    categoryForm.value.name = category || '';
  }
  
  function cancelEditCategory() {
    editingCategory.value = null;
    editingCategoryName.value = '';
    categoryForm.value.name = '';
  }
  
  function saveCategory() {
    if (editingCategory.value === 'new') {
      if (!categories.value.includes(categoryForm.value.name)) {
        categories.value.push(categoryForm.value.name);
        stats.value.totalCategories++;
      }
    } else {
      const index = categories.value.findIndex(c => c === editingCategory.value);
      if (index > -1) {
        categories.value[index] = categoryForm.value.name;
      }
    }
    cancelEditCategory();
  }
  
  function deleteCategory(category) {
    if (category !== 'All' && confirm('Delete this category?')) {
      categories.value = categories.value.filter(c => c !== category);
      stats.value.totalCategories--;
      // Optionally remove from posts
    }
  }
  
  // User functions
  function startEditUser(user) {
    editingUserId.value = user ? user.id : 'new';
    editingUser.value = user;
    userForm.value = user ? { ...user } : { name: '', email: '', role: 'Author' };
  }
  
  function cancelEditUser() {
    editingUserId.value = null;
    editingUser.value = null;
    userForm.value = { name: '', email: '', role: 'Author' };
  }
  
  function saveUser() {
    if (editingUser.value) {
      const index = users.value.findIndex(u => u.id === editingUser.value.id);
      users.value[index] = { ...userForm.value, id: editingUser.value.id };
    } else {
      const newUser = { ...userForm.value, id: Date.now() };
      users.value.unshift(newUser);
      stats.value.totalUsers++;
    }
    cancelEditUser();
  }
  
  function deleteUser(id) {
    if (confirm('Delete this user?')) {
      users.value = users.value.filter(u => u.id !== id);
      stats.value.totalUsers--;
    }
  }
  
  // Head
  useHead({
    title: 'Admin - WebDevLab',
    meta: [{ name: 'description', content: 'Admin panel for managing blog content and users.' }],
  });
  </script>
  
  <style scoped>
  .line-clamp-1 {
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  
  /* Reuse animations from home */
  @keyframes float-slow {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(5deg); }
  }
  @keyframes float-medium {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-15px) rotate(-3deg); }
  }
  @keyframes float-fast {
    0%, 100% { transform: translateY(0) scale(1); }
    50% { transform: translateY(-10px) scale(1.05); }
  }
  @keyframes fade-in-up {
    0% { opacity: 0; transform: translateY(30px); }
    100% { opacity: 1; transform: translateY(0); }
  }
  
  .animate-float-slow { animation: float-slow 10s ease-in-out infinite; }
  .animate-float-medium { animation: float-medium 8s ease-in-out infinite; }
  .animate-float-fast { animation: float-fast 6s ease-in-out infinite; }
  .animate-fade-in-up { animation: fade-in-up 0.8s ease-out forwards; opacity: 0; }
  </style>