<template>
    <div class="card p-8 text-center group cursor-pointer" @click="navigateTo(link)">
      <div class="text-4xl mb-4 transform group-hover:scale-110 transition-transform duration-200">
        {{ icon }}
      </div>
      <h3 class="text-xl font-bold text-gray-900 mb-3">{{ title }}</h3>
      <p class="text-gray-600 mb-6 leading-relaxed">{{ description }}</p>
      <div 
        class="inline-flex items-center text-sm font-medium transition-colors duration-200"
        :class="colorClasses"
      >
        Learn More
        <svg class="ml-2 h-4 w-4 transform group-hover:translate-x-1 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
        </svg>
      </div>
    </div>
  </template>
  
  <script setup>
  const { icon, title, description, link, color = 'primary' } = defineProps({
    icon: String,
    title: String,
    description: String,
    link: String,
    color: {
      type: String,
      default: 'primary'
    }
  })
  
  const colorClasses = computed(() => {
    const colors = {
      primary: 'text-primary-600 group-hover:text-primary-700',
      secondary: 'text-secondary-600 group-hover:text-secondary-700',
      accent: 'text-accent-600 group-hover:text-accent-700'
    }
    return colors[color] || colors.primary
  })
  </script>