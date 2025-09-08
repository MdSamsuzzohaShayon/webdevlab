<template>
    <div class="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100">
  
      <!-- Hero Section -->
      <section class="relative py-16 md:py-24 overflow-hidden">
        <div class="absolute top-0 left-0 w-full h-full opacity-5">
          <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <pattern id="smallGrid" width="20" height="20" patternUnits="userSpaceOnUse">
                <path d="M 20 0 L 0 0 0 20" fill="none" stroke="currentColor" stroke-width="0.5" />
              </pattern>
            </defs>
            <rect width="100%" height="100%" fill="url(#smallGrid)" />
          </svg>
        </div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
          <div class="text-center max-w-3xl mx-auto">
            <h1 class="text-4xl md:text-6xl font-bold text-gray-900 mb-6">
              WebDevLab <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-secondary-600">Blog</span>
            </h1>
            <p class="text-xl text-gray-600 mb-8">
              Insights, tutorials and trends in web development, AI, blockchain, and more.
            </p>
            
            <!-- Search and Filter -->
            <div class="relative max-w-xl mx-auto mb-12">
              <input 
                type="text" 
                placeholder="Search articles..." 
                class="w-full px-6 py-4 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-primary-300 shadow-sm"
                v-model="searchQuery"
              >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-400 absolute right-4 top-1/2 transform -translate-y-1/2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
            
            <!-- Category Filter -->
            <div class="flex flex-wrap justify-center gap-3 mb-12">
              <button 
                v-for="category in categories" 
                :key="category" 
                @click="toggleCategory(category)"
                :class="{'bg-gradient-to-r from-primary-500 to-secondary-500 text-white': selectedCategories.includes(category), 'bg-white text-gray-700 hover:bg-gray-50': !selectedCategories.includes(category)}"
                class="px-4 py-2 rounded-full border border-gray-200 transition-all duration-200 shadow-sm"
              >
                {{ category }}
              </button>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Blog Posts -->
      <section class="py-12 pb-20 relative">
        <!-- Animated background elements -->
        <div class="absolute top-40 -left-20 w-72 h-72 bg-primary-100 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse"></div>
        <div class="absolute top-80 -right-20 w-72 h-72 bg-secondary-100 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse" style="animation-delay: 2s"></div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <article 
              v-for="(post, index) in filteredPosts" 
              :key="post.id"
              class="card group overflow-hidden hover:shadow-lg transition-all duration-300"
              :style="`animation-delay: ${index * 0.1}s`"
            >
              <div class="relative overflow-hidden">
                <div 
                  class="aspect-video w-full bg-gradient-to-r" 
                  :class="post.gradient"
                ></div>
                <div class="absolute top-4 left-4">
                  <span class="px-3 py-1 text-xs font-medium rounded-full text-white bg-black/30 backdrop-blur-sm">
                    {{ post.category }}
                  </span>
                </div>
              </div>
              
              <div class="p-6">
                <div class="flex items-center text-sm text-gray-500 mb-3">
                  <span>{{ post.date }}</span>
                  <span class="mx-2">•</span>
                  <span>{{ post.readTime }} read</span>
                </div>
                
                <h3 class="text-xl font-semibold text-gray-900 mb-3 group-hover:text-primary-600 transition-colors">
                  {{ post.title }}
                </h3>
                
                <p class="text-gray-600 mb-4">
                  {{ post.excerpt }}
                </p>
                
                <div class="flex items-center justify-between">
                  <div class="flex items-center">
                    <div class="w-8 h-8 rounded-full bg-gray-200 mr-3"></div>
                    <span class="text-sm font-medium text-gray-700">{{ post.author }}</span>
                  </div>
                  
                  <NuxtLink 
                    :to="`/blog/${post.slug}`" 
                    class="text-primary-600 hover:text-primary-700 font-medium flex items-center transition-colors"
                  >
                    Read more
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                    </svg>
                  </NuxtLink>
                </div>
              </div>
            </article>
          </div>
          
          <!-- Empty state -->
          <div v-if="filteredPosts.length === 0" class="text-center py-12">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 mx-auto text-gray-400 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <h3 class="text-xl font-medium text-gray-900 mb-2">No articles found</h3>
            <p class="text-gray-600">Try adjusting your search or filter criteria</p>
          </div>
        </div>
      </section>
  
      <!-- Newsletter CTA -->
      <section class="py-16 bg-gradient-to-r from-primary-600 to-secondary-600">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 class="text-3xl font-bold text-white mb-4">Never Miss an Article</h2>
          <p class="text-primary-100 text-lg mb-8">
            Get the latest articles on web development, AI, blockchain, and more delivered to your inbox.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 max-w-lg mx-auto">
            <input
              type="email"
              placeholder="Enter your email"
              class="flex-1 px-4 py-3 rounded-lg border-0 focus:outline-none focus:ring-2 focus:ring-primary-300"
            />
            <button
              class="bg-white text-primary-600 font-semibold px-8 py-3 rounded-lg hover:bg-gray-50 transition-colors duration-200"
            >
              Subscribe
            </button>
          </div>
        </div>
      </section>

    </div>
  </template>
  
  <script setup>
  // Blog posts data
  const posts = [
    {
      id: 1,
      title: "Understanding Web3: The Decentralized Future of the Internet",
      excerpt: "Explore how Web3 is transforming digital interactions through blockchain, decentralization, and token-based economics.",
      category: "Web3",
      date: "May 15, 2023",
      readTime: "8 min",
      author: "Sarah Johnson",
      slug: "understanding-web3-decentralized-future",
      gradient: "from-purple-500 to-indigo-600"
    },
    {
      id: 2,
      title: "AI-Powered Development: Revolutionizing How We Build Software",
      excerpt: "Discover how artificial intelligence is changing the landscape of software development with code generation and automated testing.",
      category: "AI",
      date: "April 28, 2023",
      readTime: "10 min",
      author: "Michael Chen",
      slug: "ai-powered-development-revolution",
      gradient: "from-cyan-500 to-blue-600"
    },
    {
      id: 3,
      title: "Mobile Development in 2023: Cross-Platform vs Native",
      excerpt: "A comprehensive comparison of development approaches for mobile applications in the current ecosystem.",
      category: "Mobile",
      date: "April 12, 2023",
      readTime: "6 min",
      author: "Jessica Williams",
      slug: "mobile-development-2023-cross-platform-vs-native",
      gradient: "from-green-500 to-teal-600"
    },
    {
      id: 4,
      title: "Scaling Backend Systems: Strategies for High Traffic Applications",
      excerpt: "Learn essential techniques for building backend systems that can handle millions of users without breaking a sweat.",
      category: "Backend",
      date: "March 30, 2023",
      readTime: "12 min",
      author: "David Kim",
      slug: "scaling-backend-systems-strategies",
      gradient: "from-red-500 to-orange-600"
    },
    {
      id: 5,
      title: "The Complete Full Stack Developer Roadmap 2023",
      excerpt: "A step-by-step guide to becoming a proficient full stack developer with the most relevant technologies this year.",
      category: "Full Stack",
      date: "March 18, 2023",
      readTime: "15 min",
      author: "Alex Rodriguez",
      slug: "complete-full-stack-developer-roadmap-2023",
      gradient: "from-yellow-500 to-amber-600"
    },
    {
      id: 6,
      title: "Smart Contracts 101: Building on Ethereum and Solidity",
      excerpt: "An introduction to creating and deploying smart contracts on the Ethereum blockchain using Solidity.",
      category: "Web3",
      date: "March 5, 2023",
      readTime: "9 min",
      author: "Emma Thompson",
      slug: "smart-contracts-101-ethereum-solidity",
      gradient: "from-violet-500 to-purple-600"
    }
  ];
  
  // Categories
  const categories = ['All', 'Web3', 'AI', 'Mobile', 'Backend', 'Full Stack'];
  
  // Reactive state
  const searchQuery = ref('');
  const selectedCategories = ref(['All']);
  
  // Filter posts based on search and categories
  const filteredPosts = computed(() => {
    return posts.filter(post => {
      const matchesSearch = post.title.toLowerCase().includes(searchQuery.value.toLowerCase()) || 
                           post.excerpt.toLowerCase().includes(searchQuery.value.toLowerCase());
      
      const matchesCategory = selectedCategories.value.includes('All') || 
                             selectedCategories.value.includes(post.category);
      
      return matchesSearch && matchesCategory;
    });
  });
  
  // Toggle category filter
  function toggleCategory(category) {
    if (category === 'All') {
      selectedCategories.value = ['All'];
      return;
    }
    
    // Remove 'All' if other categories are selected
    if (selectedCategories.value.includes('All')) {
      selectedCategories.value = selectedCategories.value.filter(c => c !== 'All');
    }
    
    if (selectedCategories.value.includes(category)) {
      selectedCategories.value = selectedCategories.value.filter(c => c !== category);
      
      // If no categories selected, revert to 'All'
      if (selectedCategories.value.length === 0) {
        selectedCategories.value = ['All'];
      }
    } else {
      selectedCategories.value.push(category);
    }
  }
  
  // Set page metadata
  useHead({
    title: 'Blog - WebDevLab',
    meta: [
      {
        name: 'description',
        content: 'Explore articles on Web3, AI, mobile development, backend scaling, and full stack development at WebDevLab.'
      }
    ]
  });
  </script>
  
  <style scoped>
  .card {
    @apply bg-white rounded-xl border border-gray-200 overflow-hidden transition-all duration-300;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
  }
  
  .card:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 10px 10px -5px rgba(0, 0, 0, 0.02);
  }
  
  .animate-pulse {
    animation: pulse 6s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  }
  
  @keyframes pulse {
    0%, 100% {
      opacity: 0.2;
    }
    50% {
      opacity: 0.4;
    }
  }
  </style>