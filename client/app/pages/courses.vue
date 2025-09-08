<template>
    <div class="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      <!-- Hero Section -->
      <section class="relative overflow-hidden py-20 sm:py-32">
        <div class="absolute inset-0">
          <div class="absolute top-20 left-10 w-72 h-72 bg-primary-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse"></div>
          <div class="absolute top-40 right-10 w-72 h-72 bg-secondary-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse" style="animation-delay: 2s"></div>
          <div class="absolute bottom-20 left-1/2 w-72 h-72 bg-accent-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse" style="animation-delay: 4s"></div>
        </div>
  
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h1 class="text-4xl sm:text-6xl font-bold text-gray-900 mb-6 animate-fade-in">
            Expand Your <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-secondary-600">Knowledge</span>
          </h1>
          <p class="text-xl text-gray-600 mb-8 max-w-3xl mx-auto animate-slide-up">
            Master in-demand skills with our expert-led courses. From Web3 to AI, mobile development to backend scaling, we have the perfect learning path for you.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center animate-slide-up" style="animation-delay: 0.3s">
            <button class="btn-primary text-lg px-8 py-4">
              Browse All Courses
            </button>
            <button class="btn-outline text-lg px-8 py-4">
              View Learning Paths
            </button>
          </div>
        </div>
      </section>
  
      <!-- Courses Grid -->
      <section class="relative py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <!-- Filter buttons -->
          <div class="flex flex-wrap justify-center mb-12 gap-3">
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
  
          <!-- Courses Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div 
              v-for="course in filteredCourses" 
              :key="course.id"
              class="card group p-6 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2"
              @mouseenter="activeCourse = course.id"
              @mouseleave="activeCourse = null"
            >
              <div class="relative mb-6">
                <div class="aspect-video rounded-xl mb-4 overflow-hidden relative">
                  <div class="w-full h-full bg-gradient-to-r" :class="course.gradient"></div>
                  <div class="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                    <button class="bg-white/90 text-primary-600 rounded-full p-3 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
                      <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                    </button>
                  </div>
                </div>
                <div class="absolute top-4 right-4 z-10">
                  <span class="px-3 py-1 text-xs font-semibold rounded-full" 
                        :class="getCategoryClass(course.category)">
                    {{ getCategoryName(course.category) }}
                  </span>
                </div>
              </div>
              
              <div class="flex items-center mb-4">
                <div class="flex items-center text-amber-500">
                  <svg v-for="star in 5" :key="star" class="w-4 h-4 fill-current" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                </div>
                <span class="ml-2 text-sm text-gray-600">({{ course.rating }})</span>
              </div>
  
              <h3 class="text-xl font-semibold text-gray-900 mb-3 group-hover:text-primary-600 transition-colors duration-200">
                {{ course.title }}
              </h3>
              <p class="text-gray-600 mb-4">{{ course.description }}</p>
              
              <div class="flex items-center justify-between mb-6">
                <div class="flex items-center">
                  <div class="w-8 h-8 rounded-full bg-gradient-to-r from-primary-500 to-secondary-500 flex items-center justify-center text-white text-xs font-bold">
                    {{ course.instructor.initials }}
                  </div>
                  <span class="ml-2 text-sm font-medium text-gray-700">{{ course.instructor.name }}</span>
                </div>
                <div class="text-right">
                  <div class="text-lg font-bold text-primary-600">${{ course.price }}</div>
                  <div v-if="course.originalPrice" class="text-sm text-gray-500 line-through">${{ course.originalPrice }}</div>
                </div>
              </div>
  
              <div class="flex items-center justify-between">
                <div class="flex items-center text-sm text-gray-600">
                  <svg class="w-4 h-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  {{ course.duration }}
                </div>
                <div class="flex items-center text-sm text-gray-600">
                  <svg class="w-4 h-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                  </svg>
                  {{ course.students }}+ enrolled
                </div>
              </div>
  
              <button class="w-full mt-6 btn-outline py-3">
                Enroll Now
              </button>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Learning Paths -->
      <section class="py-16 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-12">
            <h2 class="text-3xl font-bold text-gray-900">Structured Learning Paths</h2>
            <p class="text-gray-600 mt-4">Follow curated paths to master specific skills</p>
          </div>
  
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div v-for="path in learningPaths" :key="path.title" class="card p-6 group hover:shadow-xl transition-all duration-300">
              <div class="flex items-start mb-6">
                <div class="w-14 h-14 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-xl flex items-center justify-center mr-4 group-hover:scale-110 transition-transform duration-300">
                  <svg class="w-8 h-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="path.icon" />
                  </svg>
                </div>
                <div>
                  <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ path.title }}</h3>
                  <p class="text-gray-600">{{ path.description }}</p>
                </div>
              </div>
              
              <div class="mb-6">
                <div class="flex justify-between text-sm text-gray-600 mb-2">
                  <span>Progress</span>
                  <span>{{ path.courses.length }} courses</span>
                </div>
                <div class="w-full bg-gray-200 rounded-full h-2">
                  <div class="bg-gradient-to-r from-primary-500 to-secondary-500 h-2 rounded-full" :style="`width: ${path.progress}%`"></div>
                </div>
              </div>
              
              <div class="space-y-3">
                <div v-for="(course, index) in path.courses" :key="index" class="flex items-center">
                  <div class="flex-shrink-0 w-6 h-6 rounded-full flex items-center justify-center" :class="course.completed ? 'bg-green-500' : 'bg-gray-300'">
                    <svg v-if="course.completed" class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <span class="ml-3 text-sm" :class="course.completed ? 'text-gray-600' : 'text-gray-900 font-medium'">{{ course.title }}</span>
                </div>
              </div>
              
              <button class="w-full mt-6 btn-primary py-3">
                Start Learning Path
              </button>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Testimonials -->
      <section class="py-16 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-12">
            <h2 class="text-3xl font-bold text-gray-900">What Our Students Say</h2>
            <p class="text-gray-600 mt-4">Hear from thousands of satisfied learners</p>
          </div>
  
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div v-for="testimonial in testimonials" :key="testimonial.name" class="card p-6 group hover:shadow-xl transition-all duration-300">
              <div class="flex items-center mb-4">
                <div class="w-12 h-12 rounded-full bg-gradient-to-r from-primary-500 to-secondary-500 flex items-center justify-center text-white font-bold">
                  {{ testimonial.initials }}
                </div>
                <div class="ml-4">
                  <h4 class="font-semibold text-gray-900">{{ testimonial.name }}</h4>
                  <p class="text-sm text-gray-600">{{ testimonial.role }}</p>
                </div>
              </div>
              <div class="flex items-center mb-4">
                <div class="flex items-center text-amber-500">
                  <svg v-for="star in 5" :key="star" class="w-4 h-4 fill-current" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                </div>
              </div>
              <p class="text-gray-600 italic">"{{ testimonial.content }}"</p>
              <div class="mt-4 pt-4 border-t border-gray-100">
                <p class="text-sm text-gray-600">Completed: {{ testimonial.course }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>
  
      <!-- CTA Section -->
      <section class="py-16 bg-gradient-to-r from-primary-600 to-secondary-600">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 class="text-3xl font-bold text-white mb-4">Start Your Learning Journey Today</h2>
          <p class="text-primary-100 text-lg mb-8">
            Join thousands of students who have transformed their careers with our courses.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <button class="btn-primary bg-white text-primary-600 hover:bg-gray-100 px-8 py-4">
              Browse All Courses
            </button>
            <button class="btn-outline border-white text-white hover:bg-white hover:text-primary-600 px-8 py-4">
              Sign Up Free
            </button>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script setup>
  // Categories data
  const categories = [
    { id: 'all', name: 'All Courses' },
    { id: 'web3', name: 'Web3 & Blockchain' },
    { id: 'mobile', name: 'Mobile Development' },
    { id: 'ai', name: 'AI & Machine Learning' },
    { id: 'backend', name: 'Backend Development' },
    { id: 'fullstack', name: 'Full Stack' },
    { id: 'microservices', name: 'Microservices' }
  ];
  
  // Courses data
  const courses = [
    {
      id: 1,
      title: "Web3 Fundamentals: Blockchain & Smart Contracts",
      description: "Learn the core concepts of blockchain technology and how to build decentralized applications.",
      category: "web3",
      rating: 4.8,
      price: 89.99,
      originalPrice: 129.99,
      duration: "12 hours",
      students: 12500,
      instructor: { name: "Alex Johnson", initials: "AJ" },
      gradient: "from-purple-500 to-indigo-500"
    },
    {
      id: 2,
      title: "Advanced Mobile App Development with Flutter",
      description: "Build cross-platform mobile applications with beautiful UI and smooth performance.",
      category: "mobile",
      rating: 4.7,
      price: 79.99,
      duration: "15 hours",
      students: 8900,
      instructor: { name: "Sarah Chen", initials: "SC" },
      gradient: "from-blue-500 to-cyan-500"
    },
    {
      id: 3,
      title: "AI & Machine Learning Bootcamp",
      description: "From fundamentals to advanced techniques in artificial intelligence and ML algorithms.",
      category: "ai",
      rating: 4.9,
      price: 99.99,
      originalPrice: 149.99,
      duration: "20 hours",
      students: 15600,
      instructor: { name: "David Wilson", initials: "DW" },
      gradient: "from-green-500 to-teal-500"
    },
    {
      id: 4,
      title: "Microservices Architecture & Implementation",
      description: "Design, build and deploy scalable microservices architectures with best practices.",
      category: "microservices",
      rating: 4.8,
      price: 94.99,
      duration: "14 hours",
      students: 7200,
      instructor: { name: "Maria Garcia", initials: "MG" },
      gradient: "from-orange-500 to-red-500"
    },
    {
      id: 5,
      title: "Full Stack Web Development Masterclass",
      description: "Master both frontend and backend development with modern frameworks and tools.",
      category: "fullstack",
      rating: 4.7,
      price: 109.99,
      duration: "25 hours",
      students: 18300,
      instructor: { name: "James Smith", initials: "JS" },
      gradient: "from-pink-500 to-rose-500"
    },
    {
      id: 6,
      title: "Backend Scaling & Performance Optimization",
      description: "Learn techniques to scale your backend systems and optimize for high performance.",
      category: "backend",
      rating: 4.9,
      price: 84.99,
      originalPrice: 119.99,
      duration: "10 hours",
      students: 9500,
      instructor: { name: "Emily Davis", initials: "ED" },
      gradient: "from-amber-500 to-yellow-500"
    }
  ];
  
  // Learning paths data
  const learningPaths = [
    {
      title: "Web3 Developer Path",
      description: "Become a proficient blockchain developer",
      icon: "M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1",
      progress: 40,
      courses: [
        { title: "Blockchain Fundamentals", completed: true },
        { title: "Smart Contract Development", completed: true },
        { title: "Decentralized App (DApp) Creation", completed: false },
        { title: "Advanced Web3 Security", completed: false }
      ]
    },
    {
      title: "Full Stack Master Path",
      description: "Master both frontend and backend development",
      icon: "M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10",
      progress: 75,
      courses: [
        { title: "HTML, CSS & JavaScript", completed: true },
        { title: "React Framework", completed: true },
        { title: "Node.js & Express", completed: true },
        { title: "Database Management", completed: false }
      ]
    }
  ];
  
  // Testimonials data
  const testimonials = [
    {
      name: "Michael Rodriguez",
      initials: "MR",
      role: "Software Engineer",
      content: "The Web3 course completely transformed my career. I went from basic web development to building smart contracts in just 3 months.",
      course: "Web3 Fundamentals",
      rating: 5
    },
    {
      name: "Jessica Kim",
      initials: "JK",
      role: "Mobile Developer",
      content: "The Flutter course was incredibly comprehensive. I built my first production app within weeks of completing the course.",
      course: "Advanced Mobile App Development",
      rating: 5
    },
    {
      name: "Thomas Anderson",
      initials: "TA",
      role: "Data Scientist",
      content: "The AI Bootcamp gave me the practical skills I needed to transition from theory to real-world applications. Highly recommended!",
      course: "AI & Machine Learning Bootcamp",
      rating: 5
    }
  ];
  
  const activeCategory = ref('all');
  const activeCourse = ref(null);
  
  const filteredCourses = computed(() => {
    if (activeCategory.value === 'all') {
      return courses;
    }
    return courses.filter(course => course.category === activeCategory.value);
  });
  
  const setActiveCategory = (categoryId) => {
    activeCategory.value = categoryId;
  };
  
  const getCategoryClass = (categoryId) => {
    const classes = {
      'web3': 'bg-purple-100 text-purple-800',
      'mobile': 'bg-blue-100 text-blue-800',
      'ai': 'bg-green-100 text-green-800',
      'microservices': 'bg-orange-100 text-orange-800',
      'fullstack': 'bg-pink-100 text-pink-800',
      'backend': 'bg-amber-100 text-amber-800'
    };
    return classes[categoryId] || 'bg-gray-100 text-gray-800';
  };
  
  const getCategoryName = (categoryId) => {
    const category = categories.find(cat => cat.id === categoryId);
    return category ? category.name : 'Unknown';
  };
  
  useHead({
    title: "Courses - WebDevLab",
    meta: [
      {
        name: "description",
        content: "Explore our expert-led courses in Web3, AI, mobile development, backend scaling, and more.",
      },
    ],
  });
  </script>
  
  <style scoped>
  .card {
    @apply bg-white rounded-xl shadow-md overflow-hidden transition-all duration-300;
  }
  
  .btn-primary {
    @apply bg-gradient-to-r from-primary-600 to-secondary-600 text-white font-semibold rounded-lg shadow-md hover:shadow-lg transition-all duration-300 transform hover:-translate-y-0.5;
  }
  
  .btn-outline {
    @apply border-2 border-primary-600 text-primary-600 font-semibold rounded-lg hover:bg-primary-600 hover:text-white transition-all duration-300;
  }
  
  .animate-fade-in {
    animation: fadeIn 1s ease-out;
  }
  
  .animate-slide-up {
    animation: slideUp 0.8s ease-out;
  }
  
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  
  @keyframes slideUp {
    from { 
      opacity: 0;
      transform: translateY(20px);
    }
    to { 
      opacity: 1;
      transform: translateY(0);
    }
  }
  </style>