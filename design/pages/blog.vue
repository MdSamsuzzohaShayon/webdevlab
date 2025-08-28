<template>
    <div class="min-h-screen bg-gray-50">
      <!-- Hero Section -->
      <section class="bg-white py-16 border-b border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center">
            <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
              Developer Blog
            </h1>
            <p class="text-xl text-gray-600 max-w-3xl mx-auto">
              Insights, tutorials, and the latest trends in web development from our community of experts.
            </p>
          </div>
        </div>
      </section>
  
      <!-- Blog Content -->
      <section class="py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <!-- Filters -->
          <div class="flex flex-wrap gap-4 mb-12">
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
  
          <!-- Blog Posts Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <article 
              v-for="post in filteredPosts" 
              :key="post.id"
              class="card overflow-hidden"
            >
              <img 
                :src="post.image" 
                :alt="post.title"
                class="w-full h-48 object-cover"
              >
              <div class="p-6">
                <div class="flex items-center text-sm text-gray-500 mb-3">
                  <span class="bg-primary-100 text-primary-800 px-2 py-1 rounded-full text-xs font-medium mr-3">
                    {{ post.category }}
                  </span>
                  <span>{{ post.date }}</span>
                </div>
                <h2 class="text-xl font-bold text-gray-900 mb-3 hover:text-primary-600 transition-colors">
                  {{ post.title }}
                </h2>
                <p class="text-gray-600 mb-4">{{ post.excerpt }}</p>
                <div class="flex items-center justify-between">
                  <div class="flex items-center">
                    <img 
                      :src="post.author.avatar" 
                      :alt="post.author.name"
                      class="w-8 h-8 rounded-full mr-3"
                    >
                    <span class="text-sm text-gray-700">{{ post.author.name }}</span>
                  </div>
                  <button class="text-primary-600 hover:text-primary-700 font-medium">
                    Read More
                  </button>
                </div>
              </div>
            </article>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script setup>
  useHead({
    title: 'Blog - WebDevLab',
    meta: [
      { name: 'description', content: 'Read the latest web development tutorials, insights, and industry trends.' }
    ]
  })
  
  const selectedCategory = ref('All')
  const categories = ['All', 'JavaScript', 'React', 'Vue.js', 'Node.js', 'CSS', 'Career Tips']
  
  const posts = [
    {
      id: 1,
      title: 'Building Modern Web Applications with Vue 3',
      excerpt: 'Learn how to leverage the latest features in Vue 3 to build performant web applications.',
      category: 'Vue.js',
      date: 'Jan 15, 2025',
      image: 'https://images.pexels.com/photos/270348/pexels-photo-270348.jpeg',
      author: {
        name: 'Sarah Johnson',
        avatar: 'https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?w=100&h=100&fit=crop&crop=face'
      }
    },
    {
      id: 2,
      title: 'JavaScript ES2024: New Features You Should Know',
      excerpt: 'Discover the latest JavaScript features and how they can improve your development workflow.',
      category: 'JavaScript',
      date: 'Jan 12, 2025',
      image: 'https://images.pexels.com/photos/574071/pexels-photo-574071.jpeg',
      author: {
        name: 'Mike Chen',
        avatar: 'https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?w=100&h=100&fit=crop&crop=face'
      }
    },
    {
      id: 3,
      title: 'Career Growth: From Junior to Senior Developer',
      excerpt: 'Essential tips and strategies for advancing your career in software development.',
      category: 'Career Tips',
      date: 'Jan 10, 2025',
      image: 'https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg',
      author: {
        name: 'Alex Rivera',
        avatar: 'https://images.pexels.com/photos/712513/pexels-photo-712513.jpeg?w=100&h=100&fit=crop&crop=face'
      }
    }
  ]
  
  const filteredPosts = computed(() => {
    if (selectedCategory.value === 'All') {
      return posts
    }
    return posts.filter(post => post.category === selectedCategory.value)
  })
  </script>