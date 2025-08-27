<template>
    <div>
      <!-- Hero Section -->
      <section class="gradient-bg text-white py-20 overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center animate-fade-in">
            <h1 class="text-4xl md:text-6xl font-bold mb-6 animate-slide-up">
              Welcome to <span class="text-yellow-400">WebDevLab</span>
            </h1>
            <p class="text-xl md:text-2xl mb-8 text-blue-100 max-w-3xl mx-auto animate-slide-up" style="animation-delay: 0.2s">
              Your ultimate destination for web development learning, career growth, and community engagement.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center animate-slide-up" style="animation-delay: 0.4s">
              <button class="btn-primary bg-white text-primary-600 hover:bg-gray-100">
                Start Learning Today
              </button>
              <button class="btn-secondary bg-transparent border-white text-white hover:bg-white hover:text-primary-600">
                Explore Courses
              </button>
            </div>
          </div>
          
          <!-- Floating Elements -->
          <div class="absolute top-20 left-10 w-20 h-20 bg-yellow-400 rounded-full opacity-20 animate-bounce-gentle"></div>
          <div class="absolute top-40 right-10 w-16 h-16 bg-pink-400 rounded-full opacity-20 animate-bounce-gentle" style="animation-delay: 1s"></div>
          <div class="absolute bottom-20 left-20 w-12 h-12 bg-green-400 rounded-full opacity-20 animate-bounce-gentle" style="animation-delay: 2s"></div>
        </div>
      </section>
  
      <!-- Features Section -->
      <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-16">
            <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Everything You Need to Excel
            </h2>
            <p class="text-xl text-gray-600 max-w-3xl mx-auto">
              From beginner tutorials to advanced career guidance, we've got you covered with comprehensive resources.
            </p>
          </div>
  
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <FeatureCard
              v-for="feature in features"
              :key="feature.title"
              :icon="feature.icon"
              :title="feature.title"
              :description="feature.description"
              :link="feature.link"
              :color="feature.color"
            />
          </div>
        </div>
      </section>
  
      <!-- Stats Section -->
      <section class="py-20 bg-gray-900 text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div v-for="stat in stats" :key="stat.label">
              <div class="text-4xl font-bold text-accent-400 mb-2">{{ stat.value }}</div>
              <div class="text-gray-300">{{ stat.label }}</div>
            </div>
          </div>
        </div>
      </section>
  
      <!-- CTA Section -->
      <section class="py-20 bg-primary-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Ready to Start Your Journey?
          </h2>
          <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
            Join thousands of developers who are already advancing their careers with WebDevLab.
          </p>
          <button class="btn-primary text-lg px-8 py-4">
            Get Started Now
          </button>
        </div>
      </section>
    </div>
  </template>
  
  <script setup>
  useHead({
    title: 'WebDevLab - Learn, Code, Grow',
    meta: [
      { name: 'description', content: 'Your ultimate destination for web development learning, career growth, and community engagement.' }
    ]
  })
  
  const features = [
    {
      icon: '📝',
      title: 'Blog & Articles',
      description: 'Stay updated with the latest trends, tutorials, and insights from industry experts.',
      link: '/blog',
      color: 'primary'
    },
    {
      icon: '🎓',
      title: 'Online Courses',
      description: 'Comprehensive courses designed to take you from beginner to professional developer.',
      link: '/courses',
      color: 'secondary'
    },
    {
      icon: '💼',
      title: 'Career Portal',
      description: 'Find your dream job and advance your career with our exclusive job listings.',
      link: '/career',
      color: 'accent'
    },
    {
      icon: '👥',
      title: 'Community Forum',
      description: 'Connect with fellow developers, ask questions, and share your knowledge.',
      link: '/forum',
      color: 'primary'
    },
    {
      icon: '🎬',
      title: 'Shorts & Videos',
      description: 'Quick tutorials and tips in bite-sized video format for busy developers.',
      link: '/shorts',
      color: 'secondary'
    },
    {
      icon: '🚀',
      title: 'Exclusive Resources',
      description: 'Access premium tools, templates, and resources to accelerate your development.',
      link: '/resources',
      color: 'accent'
    }
  ]
  
  const stats = [
    { value: '10K+', label: 'Students' },
    { value: '500+', label: 'Courses' },
    { value: '1M+', label: 'Code Lines' },
    { value: '24/7', label: 'Support' }
  ]
  </script>