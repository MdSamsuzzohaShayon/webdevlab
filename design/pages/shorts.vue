<template>
    <div class="min-h-screen bg-gray-50">
      <!-- Hero Section -->
      <section class="bg-white py-16 border-b border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center">
            <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
              Developer Shorts
            </h1>
            <p class="text-xl text-gray-600 max-w-3xl mx-auto">
              Quick tips, tutorials, and insights in bite-sized video format for busy developers.
            </p>
          </div>
        </div>
      </section>
  
      <!-- Shorts Grid -->
      <section class="py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <!-- Categories Filter -->
          <div class="flex flex-wrap gap-4 mb-12 justify-center">
            <button 
              v-for="category in categories" 
              :key="category"
              class="px-4 py-2 rounded-full border border-gray-300 hover:border-primary-500 hover:text-primary-600 transition-colors"
              :class="selectedCategory === category ? 'bg-primary-600 text-white border-primary-600' : ''"
              @click="selectedCategory = category"
            >
              {{ category }}
            </button>
          </div>
  
          <!-- Shorts Grid -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <div 
              v-for="short in filteredShorts" 
              :key="short.id"
              class="card overflow-hidden group cursor-pointer"
              @click="playVideo(short)"
            >
              <div class="relative aspect-video">
                <img 
                  :src="short.thumbnail" 
                  :alt="short.title"
                  class="w-full h-full object-cover"
                >
                <div class="absolute inset-0 bg-black bg-opacity-20 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                  <div class="bg-white bg-opacity-90 rounded-full p-3">
                    <svg class="h-8 w-8 text-primary-600" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M8 5v10l8-5-8-5z" />
                    </svg>
                  </div>
                </div>
                <div class="absolute bottom-2 right-2 bg-black bg-opacity-75 text-white px-2 py-1 rounded text-sm">
                  {{ short.duration }}
                </div>
              </div>
              <div class="p-4">
                <div class="flex items-center space-x-2 mb-2">
                  <span 
                    class="px-2 py-1 text-xs font-medium rounded-full"
                    :class="getCategoryColor(short.category)"
                  >
                    {{ short.category }}
                  </span>
                  <span class="text-xs text-gray-500">{{ short.views }} views</span>
                </div>
                <h3 class="font-bold text-gray-900 mb-2 line-clamp-2">{{ short.title }}</h3>
                <div class="flex items-center">
                  <img 
                    :src="short.author.avatar" 
                    :alt="short.author.name"
                    class="w-6 h-6 rounded-full mr-2"
                  >
                  <span class="text-sm text-gray-600">{{ short.author.name }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Video Modal -->
      <div v-if="selectedVideo" class="fixed inset-0 z-50 overflow-y-auto" @click="closeVideo">
        <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <div class="fixed inset-0 bg-black bg-opacity-90" aria-hidden="true"></div>
          <div class="inline-block align-middle bg-white rounded-lg overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-4xl sm:w-full" @click.stop>
            <div class="aspect-video bg-black">
              <div class="w-full h-full flex items-center justify-center text-white">
                <div class="text-center">
                  <div class="text-6xl mb-4">▶️</div>
                  <p class="text-xl mb-2">{{ selectedVideo.title }}</p>
                  <p class="text-gray-300">Video would play here in a real implementation</p>
                </div>
              </div>
            </div>
            <div class="p-6">
              <h2 class="text-2xl font-bold text-gray-900 mb-2">{{ selectedVideo.title }}</h2>
              <p class="text-gray-600 mb-4">{{ selectedVideo.description }}</p>
              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <img 
                    :src="selectedVideo.author.avatar" 
                    :alt="selectedVideo.author.name"
                    class="w-8 h-8 rounded-full mr-3"
                  >
                  <span class="font-medium">{{ selectedVideo.author.name }}</span>
                </div>
                <button @click="closeVideo" class="btn-secondary">
                  Close
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  useHead({
    title: 'Shorts - WebDevLab',
    meta: [
      { name: 'description', content: 'Watch quick web development tutorials and tips in short video format.' }
    ]
  })
  
  const selectedCategory = ref('All')
  const selectedVideo = ref(null)
  const categories = ['All', 'JavaScript', 'CSS', 'React', 'Vue.js', 'Tips & Tricks', 'Career']
  
  const shorts = [
    {
      id: 1,
      title: '5 CSS Tricks Every Developer Should Know',
      category: 'CSS',
      duration: '2:30',
      views: '12K',
      thumbnail: 'https://images.pexels.com/photos/196644/pexels-photo-196644.jpeg',
      description: 'Learn 5 essential CSS tricks that will improve your web development workflow.',
      author: {
        name: 'CSS Master',
        avatar: 'https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?w=100&h=100&fit=crop&crop=face'
      }
    },
    {
      id: 2,
      title: 'JavaScript Array Methods in 60 Seconds',
      category: 'JavaScript',
      duration: '1:00',
      views: '8.5K',
      thumbnail: 'https://images.pexels.com/photos/270348/pexels-photo-270348.jpeg',
      description: 'Quick overview of the most useful JavaScript array methods.',
      author: {
        name: 'JS Ninja',
        avatar: 'https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?w=100&h=100&fit=crop&crop=face'
      }
    },
    {
      id: 3,
      title: 'React Hooks Explained Simply',
      category: 'React',
      duration: '3:15',
      views: '15K',
      thumbnail: 'https://images.pexels.com/photos/574071/pexels-photo-574071.jpeg',
      description: 'Understand React Hooks with simple examples and practical use cases.',
      author: {
        name: 'React Pro',
        avatar: 'https://images.pexels.com/photos/712513/pexels-photo-712513.jpeg?w=100&h=100&fit=crop&crop=face'
      }
    },
    {
      id: 4,
      title: 'Vue.js Composition API Basics',
      category: 'Vue.js',
      duration: '2:45',
      views: '9.2K',
      thumbnail: 'https://images.pexels.com/photos/276452/pexels-photo-276452.jpeg',
      description: 'Get started with Vue.js Composition API in just a few minutes.',
      author: {
        name: 'Vue Expert',
        avatar: 'https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?w=100&h=100&fit=crop&crop=face'
      }
    }
  ]
  
  const filteredShorts = computed(() => {
    if (selectedCategory.value === 'All') {
      return shorts
    }
    return shorts.filter(short => short.category === selectedCategory.value)
  })
  
  const getCategoryColor = (category) => {
    const colors = {
      JavaScript: 'bg-yellow-100 text-yellow-800',
      CSS: 'bg-blue-100 text-blue-800',
      React: 'bg-cyan-100 text-cyan-800',
      'Vue.js': 'bg-green-100 text-green-800',
      'Tips & Tricks': 'bg-purple-100 text-purple-800',
      Career: 'bg-orange-100 text-orange-800'
    }
    return colors[category] || 'bg-gray-100 text-gray-800'
  }
  
  const playVideo = (video) => {
    selectedVideo.value = video
  }
  
  const closeVideo = () => {
    selectedVideo.value = null
  }
  </script>