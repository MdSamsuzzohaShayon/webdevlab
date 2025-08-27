<template>
    <div class="min-h-screen bg-gray-50">
      <!-- Hero Section -->
      <section class="bg-white py-16 border-b border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center">
            <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
              Online Courses
            </h1>
            <p class="text-xl text-gray-600 max-w-3xl mx-auto">
              Master web development with our comprehensive courses designed by industry experts.
            </p>
          </div>
        </div>
      </section>
  
      <!-- Courses Grid -->
      <section class="py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div 
              v-for="course in courses" 
              :key="course.id"
              class="card overflow-hidden"
            >
              <img 
                :src="course.image" 
                :alt="course.title"
                class="w-full h-48 object-cover"
              >
              <div class="p-6">
                <div class="flex items-center justify-between mb-3">
                  <span 
                    class="px-3 py-1 rounded-full text-xs font-medium"
                    :class="course.level === 'Beginner' ? 'bg-green-100 text-green-800' : 
                           course.level === 'Intermediate' ? 'bg-yellow-100 text-yellow-800' : 
                           'bg-red-100 text-red-800'"
                  >
                    {{ course.level }}
                  </span>
                  <div class="flex items-center text-yellow-400">
                    <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                    </svg>
                    <span class="ml-1 text-sm text-gray-700">{{ course.rating }}</span>
                  </div>
                </div>
                
                <h3 class="text-xl font-bold text-gray-900 mb-3">{{ course.title }}</h3>
                <p class="text-gray-600 mb-4">{{ course.description }}</p>
                
                <div class="flex items-center text-sm text-gray-500 mb-4">
                  <svg class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <span class="mr-4">{{ course.duration }}</span>
                  <svg class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM9 3a2 2 0 11-4 0 2 2 0 014 0z" />
                  </svg>
                  <span>{{ course.students }} students</span>
                </div>
                
                <div class="flex items-center justify-between">
                  <div class="text-2xl font-bold text-primary-600">
                    {{ course.price === 0 ? 'Free' : `$${course.price}` }}
                  </div>
                  <button class="btn-primary">
                    Enroll Now
                  </button>
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
    title: 'Courses - WebDevLab',
    meta: [
      { name: 'description', content: 'Learn web development with our comprehensive online courses.' }
    ]
  })
  
  const courses = [
    {
      id: 1,
      title: 'Complete JavaScript Bootcamp',
      description: 'Master JavaScript from basics to advanced concepts with hands-on projects.',
      image: 'https://images.pexels.com/photos/270348/pexels-photo-270348.jpeg',
      level: 'Beginner',
      duration: '40 hours',
      students: '2.5k',
      rating: 4.8,
      price: 99
    },
    {
      id: 2,
      title: 'React Development Mastery',
      description: 'Build modern web applications with React, Redux, and modern JavaScript.',
      image: 'https://images.pexels.com/photos/574071/pexels-photo-574071.jpeg',
      level: 'Intermediate',
      duration: '35 hours',
      students: '1.8k',
      rating: 4.9,
      price: 129
    },
    {
      id: 3,
      title: 'Node.js Backend Development',
      description: 'Create scalable backend applications with Node.js, Express, and MongoDB.',
      image: 'https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg',
      level: 'Intermediate',
      duration: '45 hours',
      students: '1.2k',
      rating: 4.7,
      price: 149
    },
    {
      id: 4,
      title: 'CSS Grid & Flexbox Masterclass',
      description: 'Master modern CSS layout techniques with practical examples.',
      image: 'https://images.pexels.com/photos/196644/pexels-photo-196644.jpeg',
      level: 'Beginner',
      duration: '20 hours',
      students: '3.1k',
      rating: 4.6,
      price: 0
    },
    {
      id: 5,
      title: 'Vue.js Complete Guide',
      description: 'Learn Vue.js 3 composition API and build reactive web applications.',
      image: 'https://images.pexels.com/photos/276452/pexels-photo-276452.jpeg',
      level: 'Intermediate',
      duration: '38 hours',
      students: '950',
      rating: 4.8,
      price: 119
    },
    {
      id: 6,
      title: 'Full-Stack Development with MERN',
      description: 'Build complete web applications using MongoDB, Express, React, and Node.js.',
      image: 'https://images.pexels.com/photos/1181298/pexels-photo-1181298.jpeg',
      level: 'Advanced',
      duration: '60 hours',
      students: '720',
      rating: 4.9,
      price: 199
    }
  ]
  </script>