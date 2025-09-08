<template>
    <div>
      <!-- Hero Section -->
      <section
        class="relative overflow-hidden bg-gradient-to-br from-primary-50 via-white to-secondary-50 py-20 sm:py-32"
      >
        <div class="absolute inset-0">
          <div
            class="absolute top-20 left-10 w-72 h-72 bg-primary-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse"
          ></div>
          <div
            class="absolute top-40 right-10 w-72 h-72 bg-secondary-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse"
            style="animation-delay: 2s"
          ></div>
          <div
            class="absolute bottom-20 left-1/2 w-72 h-72 bg-accent-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse"
            style="animation-delay: 4s"
          ></div>
        </div>
  
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center">
            <h1
              class="text-4xl sm:text-6xl font-bold text-gray-900 mb-6 animate-fade-in"
            >
              About <span
                class="text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-secondary-600"
              >
                WebDevLab
              </span>
            </h1>
            <p
              class="text-xl text-gray-600 mb-8 max-w-3xl mx-auto animate-slide-up"
            >
              We're a passionate team of developers, designers, and innovators dedicated to building the digital future through cutting-edge technology and education.
            </p>
          </div>
        </div>
      </section>
  
      <!-- Mission & Values -->
      <section class="py-16 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div class="relative">
              <div class="relative z-10 rounded-2xl overflow-hidden shadow-xl">
                <div class="aspect-w-16 aspect-h-9 bg-gradient-to-r from-primary-400 to-secondary-400 rounded-2xl"></div>
              </div>
              <div
                class="absolute -bottom-6 -right-6 w-64 h-64 bg-accent-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse"
                style="animation-delay: 1s"
              ></div>
            </div>
            
            <div>
              <h2 class="text-3xl font-bold text-gray-900 mb-6">Our Mission</h2>
              <p class="text-gray-600 mb-6">
                At WebDevLab, we're on a mission to democratize technology education while delivering exceptional digital solutions. We believe that everyone should have access to the skills needed to thrive in the digital economy.
              </p>
              
              <div class="space-y-4">
                <div v-for="value in values" :key="value.title" class="flex items-start">
                  <div class="flex-shrink-0">
                    <div class="flex items-center justify-center h-10 w-10 rounded-md bg-gradient-to-r from-primary-500 to-secondary-500 text-white">
                      <component :is="value.icon" class="h-6 w-6" />
                    </div>
                  </div>
                  <div class="ml-4">
                    <h3 class="text-lg font-medium text-gray-900">{{ value.title }}</h3>
                    <p class="text-gray-600">{{ value.description }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Services Section -->
      <section class="py-16 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-12">
            <h2 class="text-3xl font-bold text-gray-900">Our Services</h2>
            <p class="text-gray-600 mt-4">Comprehensive digital solutions for the modern world</p>
          </div>
  
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div v-for="(service, index) in services" :key="service.title" 
              class="card p-6 text-center group hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2"
              :style="`animation-delay: ${index * 0.1}s`">
              <div class="inline-flex items-center justify-center p-3 mb-4 rounded-lg bg-gradient-to-r from-primary-500 to-secondary-500 text-white group-hover:scale-110 transition-transform duration-300">
                <component :is="service.icon" class="h-8 w-8" />
              </div>
              <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ service.title }}</h3>
              <p class="text-gray-600">{{ service.description }}</p>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Team Section -->
      <section class="py-16 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-12">
            <h2 class="text-3xl font-bold text-gray-900">Meet Our Team</h2>
            <p class="text-gray-600 mt-4">Talented professionals driving innovation</p>
          </div>
  
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            <div v-for="(member, index) in team" :key="member.name" 
              class="text-center group cursor-pointer"
              @mouseenter="activeMember = index"
              @mouseleave="activeMember = null">
              <div class="relative mb-4 rounded-full overflow-hidden inline-block">
                <div class="aspect-square w-48 bg-gradient-to-r from-primary-400 to-secondary-400 rounded-full"></div>
                <div class="absolute inset-0 bg-gradient-to-r from-primary-600 to-secondary-600 opacity-0 group-hover:opacity-70 transition-opacity duration-300 flex items-center justify-center">
                  <div class="flex space-x-4">
                    <a v-for="social in member.socials" :key="social.name" :href="social.url" class="text-white hover:text-accent-300 transition-colors duration-200">
                      <component :is="social.icon" class="h-6 w-6" />
                    </a>
                  </div>
                </div>
              </div>
              <h3 class="text-xl font-semibold text-gray-900">{{ member.name }}</h3>
              <p class="text-primary-600 font-medium">{{ member.role }}</p>
              <p class="text-gray-600 mt-2">{{ member.bio }}</p>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Stats Section -->
      <section class="py-16 bg-gradient-to-r from-primary-600 to-secondary-600 text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div v-for="stat in stats" :key="stat.label" class="p-6">
              <div class="text-4xl md:text-5xl font-bold mb-2">{{ stat.value }}</div>
              <div class="text-primary-100">{{ stat.label }}</div>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Community Section -->
      <section class="py-16 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 class="text-3xl font-bold text-gray-900 mb-6">Join Our Community</h2>
              <p class="text-gray-600 mb-6">
                We believe in the power of community-driven learning and development. Our platform brings together developers, designers, and tech enthusiasts from around the world.
              </p>
              
              <ul class="space-y-4 mb-8">
                <li v-for="feature in communityFeatures" :key="feature" class="flex items-start">
                  <svg class="h-6 w-6 text-primary-500 mr-2 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                  <span class="text-gray-600">{{ feature }}</span>
                </li>
              </ul>
              
              <button class="btn-primary">Join Community</button>
            </div>
            
            <div class="relative">
              <div class="relative z-10 rounded-2xl overflow-hidden shadow-xl">
                <div class="aspect-w-16 aspect-h-12 bg-gradient-to-r from-accent-400 to-primary-400 rounded-2xl"></div>
              </div>
              <div
                class="absolute -top-6 -left-6 w-64 h-64 bg-secondary-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse"
                style="animation-delay: 3s"
              ></div>
            </div>
          </div>
        </div>
      </section>
  
      <!-- CTA Section -->
      <section class="py-16 bg-white">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 class="text-3xl font-bold text-gray-900 mb-4">Ready to Start Your Project?</h2>
          <p class="text-gray-600 text-lg mb-8">
            Let's collaborate to bring your ideas to life with cutting-edge technology and exceptional design.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <button class="btn-primary text-lg px-8 py-4">Get in Touch</button>
            <button class="btn-outline text-lg px-8 py-4">View Our Work</button>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script setup>
  // Import icons (in a real project, you would use actual icon components)
  // For demonstration, using simple div elements
  const values = [
    {
      title: "Innovation",
      description: "We stay ahead of the curve by embracing emerging technologies and methodologies.",
      icon: "div"
    },
    {
      title: "Education",
      description: "We believe in sharing knowledge and empowering others through learning.",
      icon: "div"
    },
    {
      title: "Excellence",
      description: "We're committed to delivering exceptional quality in everything we create.",
      icon: "div"
    },
    {
      title: "Community",
      description: "We foster collaboration and connection among technology enthusiasts.",
      icon: "div"
    }
  ];
  
  const services = [
    {
      title: "Web Development",
      description: "Modern, responsive websites and web applications built with cutting-edge technologies.",
      icon: "div"
    },
    {
      title: "AI Solutions",
      description: "Intelligent systems and machine learning solutions to transform your business.",
      icon: "div"
    },
    {
      title: "Mobile Apps",
      description: "Native and cross-platform mobile applications for iOS and Android.",
      icon: "div"
    },
    {
      title: "Web3 & Blockchain",
      description: "Decentralized applications and blockchain integration services.",
      icon: "div"
    }
  ];
  
  const team = [
    {
      name: "Alex Johnson",
      role: "CEO & Founder",
      bio: "Full-stack developer with passion for education and open-source.",
      socials: [
        { name: "twitter", url: "#", icon: "div" },
        { name: "linkedin", url: "#", icon: "div" },
        { name: "github", url: "#", icon: "div" }
      ]
    },
    {
      name: "Sarah Chen",
      role: "Lead Designer",
      bio: "UI/UX expert focused on creating intuitive user experiences.",
      socials: [
        { name: "twitter", url: "#", icon: "div" },
        { name: "dribbble", url: "#", icon: "div" },
        { name: "behance", url: "#", icon: "div" }
      ]
    },
    {
      name: "Marcus Rivera",
      role: "AI Specialist",
      bio: "Machine learning engineer with background in data science.",
      socials: [
        { name: "twitter", url: "#", icon: "div" },
        { name: "linkedin", url: "#", icon: "div" },
        { name: "medium", url: "#", icon: "div" }
      ]
    },
    {
      name: "Jessica Wong",
      role: "Mobile Developer",
      bio: "Cross-platform app developer with focus on performance.",
      socials: [
        { name: "twitter", url: "#", icon: "div" },
        { name: "github", url: "#", icon: "div" },
        { name: "linkedin", url: "#", icon: "div" }
      ]
    }
  ];
  
  const stats = [
    { value: "50+", label: "Projects Completed" },
    { value: "15+", label: "Team Members" },
    { value: "5+", label: "Years Experience" },
    { value: "10K+", label: "Community Members" }
  ];
  
  const communityFeatures = [
    "Weekly tech talks and workshops",
    "Exclusive learning resources",
    "Networking events with industry leaders",
    "Collaborative project opportunities",
    "Job board with exclusive listings"
  ];
  
  const activeMember = ref(null);
  
  useHead({
    title: "About WebDevLab - Technology Agency & Learning Community",
    meta: [
      {
        name: "description",
        content: "Learn about WebDevLab, a technology agency specializing in web development, AI, mobile apps, and Web3 solutions while building a learning community.",
      },
    ],
  });
  </script>
  
  <style scoped>
  .card {
    @apply bg-white rounded-2xl shadow-lg border border-gray-100;
  }
  
  .btn-primary {
    @apply inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-gradient-to-r from-primary-600 to-secondary-600 hover:from-primary-700 transition-all duration-200;
  }
  
  .btn-outline {
    @apply inline-flex items-center justify-center px-6 py-3 border border-gray-300 text-base font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 transition-all duration-200;
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