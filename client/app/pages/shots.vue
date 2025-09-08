<template>
    <div class="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 py-12 px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <header class="max-w-7xl mx-auto mb-16 text-center">
        <h1 class="text-4xl font-bold text-gray-900 mb-4">Web Dev Lab Shots</h1>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Discover the latest in web development, AI innovations, and Web3 technologies. Explore creative solutions and cutting-edge projects.
        </p>
        
        <!-- Filter buttons -->
        <div class="flex flex-wrap justify-center mt-8 gap-3">
          <button 
            v-for="category in categories" 
            :key="category.id"
            @click="setActiveCategory(category.id)"
            :class="[
              'px-4 py-2 rounded-full text-sm font-medium transition-all duration-200',
              activeCategory === category.id 
                ? 'bg-indigo-600 text-white shadow-md' 
                : 'bg-white text-gray-700 hover:bg-gray-100 shadow-sm'
            ]"
          >
            {{ category.name }}
          </button>
        </div>
      </header>
  
      <!-- Shots Grid -->
      <main class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <div 
            v-for="shot in filteredShots" 
            :key="shot.id"
            class="bg-white rounded-xl overflow-hidden shadow-md hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1"
          >
            <!-- Shot Image -->
            <div class="h-48 overflow-hidden relative">
              <div class="absolute top-4 right-4 z-10">
                <span class="px-2 py-1 text-xs font-semibold rounded-full" 
                      :class="getCategoryClass(shot.category)">
                  {{ getCategoryName(shot.category) }}
                </span>
              </div>
              <div class="w-full h-full bg-gradient-to-r" :class="shot.gradient"></div>
            </div>
            
            <!-- Shot Content -->
            <div class="p-6">
              <h3 class="text-xl font-bold text-gray-900 mb-2">{{ shot.title }}</h3>
              <p class="text-gray-600 mb-4">{{ shot.description }}</p>
              
              <!-- Tags -->
              <div class="flex flex-wrap gap-2 mb-5">
                <span 
                  v-for="(tag, index) in shot.tags" 
                  :key="index"
                  class="text-xs font-medium text-gray-500 bg-gray-100 px-2 py-1 rounded"
                >
                  #{{ tag }}
                </span>
              </div>
              
              <!-- Footer -->
              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <div class="w-8 h-8 rounded-full bg-gradient-to-r from-cyan-500 to-blue-500"></div>
                  <span class="ml-2 text-sm font-medium text-gray-700">{{ shot.author }}</span>
                </div>
                <div class="flex items-center space-x-4">
                  <div class="flex items-center text-gray-500">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                    </svg>
                    <span class="text-sm">{{ shot.likes }}</span>
                  </div>
                  <div class="flex items-center text-gray-500">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                    </svg>
                    <span class="text-sm">{{ shot.comments }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
  
      <!-- Load More Button -->
      <div class="max-w-7xl mx-auto mt-16 text-center">
        <button class="bg-white text-indigo-600 font-semibold py-3 px-8 rounded-full shadow-md hover:shadow-lg transition-all duration-300 border border-indigo-100 hover:border-indigo-200">
          Load More Shots
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ShotsPage',
    data() {
      return {
        activeCategory: 'all',
        categories: [
          { id: 'all', name: 'All Shots' },
          { id: 'webdev', name: 'Web Development' },
          { id: 'ai', name: 'Artificial Intelligence' },
          { id: 'web3', name: 'Web3 & Blockchain' },
          { id: 'uiux', name: 'UI/UX Design' }
        ],
        shots: [
          {
            id: 1,
            title: "Next.js E-commerce Dashboard",
            description: "A modern dashboard for e-commerce analytics with real-time data visualization.",
            category: "webdev",
            tags: ["nextjs", "tailwind", "dashboard", "react"],
            author: "Alex Johnson",
            likes: 243,
            comments: 42,
            gradient: "from-purple-400 to-pink-500"
          },
          {
            id: 2,
            title: "AI-Powered Code Review",
            description: "Machine learning model that automatically reviews code and suggests improvements.",
            category: "ai",
            tags: ["machinelearning", "ai", "python", "github"],
            author: "Sarah Chen",
            likes: 187,
            comments: 31,
            gradient: "from-green-400 to-cyan-500"
          },
          {
            id: 3,
            title: "NFT Marketplace UI",
            description: "A sleek interface for browsing and trading digital art NFTs on the Ethereum blockchain.",
            category: "web3",
            tags: ["nft", "ethereum", "web3", "crypto"],
            author: "Marcus Web3",
            likes: 321,
            comments: 56,
            gradient: "from-orange-400 to-red-500"
          },
          {
            id: 4,
            title: "Neural Network Visualization",
            description: "Interactive 3D visualization of neural network architectures and training processes.",
            category: "ai",
            tags: ["ai", "visualization", "threejs", "ml"],
            author: "DataVisual",
            likes: 276,
            comments: 38,
            gradient: "from-blue-400 to-indigo-500"
          },
          {
            id: 5,
            title: "Decentralized Voting System",
            description: "Blockchain-based voting platform ensuring transparency and security in elections.",
            category: "web3",
            tags: ["blockchain", "voting", "solidity", "web3"],
            author: "CryptoVote",
            likes: 198,
            comments: 29,
            gradient: "from-teal-400 to-blue-500"
          },
          {
            id: 6,
            title: "Responsive Design System",
            description: "Comprehensive design system with accessibility and dark mode support.",
            category: "uiux",
            tags: ["design", "ui", "ux", "accessibility"],
            author: "DesignGuru",
            likes: 312,
            comments: 47,
            gradient: "from-pink-400 to-rose-500"
          },
          {
            id: 7,
            title: "AI Content Generator",
            description: "GPT-3 powered tool that creates blog posts and social media content automatically.",
            category: "ai",
            tags: ["gpt3", "ai", "content", "nlp"],
            author: "AICreative",
            likes: 265,
            comments: 41,
            gradient: "from-amber-400 to-orange-500"
          },
          {
            id: 8,
            title: "Web3 Social Platform",
            description: "Decentralized social media platform where users own and control their data.",
            category: "web3",
            tags: ["social", "web3", "decentralized", "dapp"],
            author: "Web3Builder",
            likes: 229,
            comments: 33,
            gradient: "from-lime-400 to-emerald-500"
          },
          {
            id: 9,
            title: "React Component Library",
            description: "Collection of reusable React components with full TypeScript support.",
            category: "webdev",
            tags: ["react", "typescript", "components", "library"],
            author: "ReactDev",
            likes: 194,
            comments: 28,
            gradient: "from-cyan-400 to-sky-500"
          }
        ]
      }
    },
    computed: {
      filteredShots() {
        if (this.activeCategory === 'all') {
          return this.shots;
        }
        return this.shots.filter(shot => shot.category === this.activeCategory);
      }
    },
    methods: {
      setActiveCategory(categoryId) {
        this.activeCategory = categoryId;
      },
      getCategoryClass(categoryId) {
        const classes = {
          'webdev': 'bg-blue-100 text-blue-800',
          'ai': 'bg-purple-100 text-purple-800',
          'web3': 'bg-green-100 text-green-800',
          'uiux': 'bg-pink-100 text-pink-800'
        };
        return classes[categoryId] || 'bg-gray-100 text-gray-800';
      },
      getCategoryName(categoryId) {
        const category = this.categories.find(cat => cat.id === categoryId);
        return category ? category.name : 'Unknown';
      }
    }
  }
  </script>
  
  <style>
  /* Smooth transitions for all interactive elements */
  button, .shadow-md {
    transition: all 0.3s ease;
  }
  
  /* Hover effects for cards */
  .hover\:-translate-y-1:hover {
    transform: translateY(-4px);
  }
  
  /* Gradient animation on hover for cards */
  .bg-gradient-to-r {
    background-size: 200% 200%;
    transition: background-position 0.5s ease;
  }
  
  .bg-gradient-to-r:hover {
    background-position: 100% 100%;
  }
  </style>