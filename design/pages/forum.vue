<template>
    <div class="min-h-screen bg-gray-50">
      <!-- Hero Section -->
      <section class="bg-white py-16 border-b border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center">
            <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
              Community Forum
            </h1>
            <p class="text-xl text-gray-600 max-w-3xl mx-auto mb-8">
              Connect with fellow developers, ask questions, and share your knowledge with the community.
            </p>
            <button class="btn-primary">
              Start New Discussion
            </button>
          </div>
        </div>
      </section>
  
      <!-- Forum Content -->
      <section class="py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-1 lg:grid-cols-4 gap-8">
            <!-- Categories Sidebar -->
            <div class="lg:col-span-1">
              <div class="bg-white rounded-lg shadow-sm p-6">
                <h3 class="text-lg font-bold text-gray-900 mb-4">Categories</h3>
                <div class="space-y-2">
                  <a 
                    v-for="category in categories" 
                    :key="category.name"
                    href="#"
                    class="flex items-center justify-between p-3 rounded-lg hover:bg-gray-50 transition-colors"
                  >
                    <div class="flex items-center">
                      <div 
                        class="w-3 h-3 rounded-full mr-3"
                        :class="category.color"
                      ></div>
                      <span class="text-gray-700">{{ category.name }}</span>
                    </div>
                    <span class="text-sm text-gray-500">{{ category.count }}</span>
                  </a>
                </div>
              </div>
            </div>
  
            <!-- Discussion Threads -->
            <div class="lg:col-span-3">
              <div class="space-y-4">
                <div 
                  v-for="thread in threads" 
                  :key="thread.id"
                  class="card p-6"
                >
                  <div class="flex items-start space-x-4">
                    <img 
                      :src="thread.author.avatar" 
                      :alt="thread.author.name"
                      class="w-12 h-12 rounded-full"
                    >
                    <div class="flex-1">
                      <div class="flex items-center space-x-2 mb-2">
                        <span 
                          class="px-2 py-1 text-xs font-medium rounded-full"
                          :class="getCategoryColor(thread.category)"
                        >
                          {{ thread.category }}
                        </span>
                        <span class="text-sm text-gray-500">{{ thread.createdAt }}</span>
                      </div>
                      <h3 class="text-lg font-bold text-gray-900 mb-2 hover:text-primary-600 cursor-pointer">
                        {{ thread.title }}
                      </h3>
                      <p class="text-gray-600 mb-3">{{ thread.excerpt }}</p>
                      <div class="flex items-center text-sm text-gray-500">
                        <span class="mr-4">{{ thread.author.name }}</span>
                        <span class="mr-4">{{ thread.replies }} replies</span>
                        <span>{{ thread.views }} views</span>
                      </div>
                    </div>
                    <div class="text-right">
                      <div class="text-sm text-gray-500 mb-1">Last reply</div>
                      <div class="text-sm font-medium text-gray-900">{{ thread.lastReply }}</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script setup>
  useHead({
    title: 'Forum - WebDevLab',
    meta: [
      { name: 'description', content: 'Join the WebDevLab community forum to connect with other developers.' }
    ]
  })
  
  const categories = [
    { name: 'JavaScript', count: 245, color: 'bg-yellow-400' },
    { name: 'React', count: 189, color: 'bg-blue-400' },
    { name: 'Vue.js', count: 156, color: 'bg-green-400' },
    { name: 'Node.js', count: 134, color: 'bg-purple-400' },
    { name: 'CSS', count: 298, color: 'bg-pink-400' },
    { name: 'Career', count: 87, color: 'bg-orange-400' },
    { name: 'General', count: 432, color: 'bg-gray-400' }
  ]
  
  const threads = [
    {
      id: 1,
      title: 'Best practices for state management in React applications',
      excerpt: 'I\'m working on a large React application and struggling with state management. What are the current best practices?',
      category: 'React',
      author: {
        name: 'John Doe',
        avatar: 'https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?w=100&h=100&fit=crop&crop=face'
      },
      replies: 23,
      views: 1240,
      createdAt: '2 hours ago',
      lastReply: '15 min ago'
    },
    {
      id: 2,
      title: 'How to optimize Vue.js app performance?',
      excerpt: 'My Vue.js application is getting slow as it grows. Looking for optimization techniques and best practices.',
      category: 'Vue.js',
      author: {
        name: 'Sarah Smith',
        avatar: 'https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?w=100&h=100&fit=crop&crop=face'
      },
      replies: 18,
      views: 892,
      createdAt: '5 hours ago',
      lastReply: '1 hour ago'
    },
    {
      id: 3,
      title: 'Career transition from backend to full-stack developer',
      excerpt: 'I\'ve been working as a backend developer for 3 years. What should I focus on to become a full-stack developer?',
      category: 'Career',
      author: {
        name: 'Mike Johnson',
        avatar: 'https://images.pexels.com/photos/712513/pexels-photo-712513.jpeg?w=100&h=100&fit=crop&crop=face'
      },
      replies: 31,
      views: 1890,
      createdAt: '1 day ago',
      lastReply: '3 hours ago'
    }
  ]
  
  const getCategoryColor = (category) => {
    const colors = {
      JavaScript: 'bg-yellow-100 text-yellow-800',
      React: 'bg-blue-100 text-blue-800',
      'Vue.js': 'bg-green-100 text-green-800',
      'Node.js': 'bg-purple-100 text-purple-800',
      CSS: 'bg-pink-100 text-pink-800',
      Career: 'bg-orange-100 text-orange-800',
      General: 'bg-gray-100 text-gray-800'
    }
    return colors[category] || colors.General
  }
  </script>