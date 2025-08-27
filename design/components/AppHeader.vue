<template>
    <header class="bg-white shadow-sm sticky top-0 z-50">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <!-- Logo -->
          <NuxtLink to="/" class="flex items-center space-x-2">
            <div class="w-8 h-8 gradient-bg rounded-lg flex items-center justify-center">
              <span class="text-white font-bold">W</span>
            </div>
            <span class="text-xl font-bold text-gray-900">WebDevLab</span>
          </NuxtLink>
  
          <!-- Desktop Navigation -->
          <div class="hidden md:flex items-center space-x-8">
            <NuxtLink 
              v-for="item in navigation" 
              :key="item.name"
              :to="item.href" 
              class="text-gray-700 hover:text-primary-600 font-medium transition-colors duration-200"
            >
              {{ item.name }}
            </NuxtLink>
          </div>
  
          <!-- CTA Button -->
          <div class="hidden md:flex items-center space-x-4">
            <button class="btn-primary">
              Start Learning
            </button>
          </div>
  
          <!-- Mobile menu button -->
          <div class="md:hidden">
            <button @click="mobileMenuOpen = !mobileMenuOpen" class="text-gray-700 hover:text-primary-600">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
        </div>
  
        <!-- Mobile Navigation -->
        <div v-show="mobileMenuOpen" class="md:hidden py-4 border-t border-gray-200">
          <div class="flex flex-col space-y-4">
            <NuxtLink 
              v-for="item in navigation" 
              :key="item.name"
              :to="item.href" 
              class="text-gray-700 hover:text-primary-600 font-medium"
              @click="mobileMenuOpen = false"
            >
              {{ item.name }}
            </NuxtLink>
            <button class="btn-primary w-full">
              Start Learning
            </button>
          </div>
        </div>
      </nav>
    </header>
  </template>
  
  <script setup>
  const mobileMenuOpen = ref(false)
  
  const navigation = [
    { name: 'Home', href: '/' },
    { name: 'Blog', href: '/blog' },
    { name: 'Courses', href: '/courses' },
    { name: 'Career', href: '/career' },
    { name: 'Forum', href: '/forum' },
    { name: 'Shorts', href: '/shorts' },
  ]
  </script>