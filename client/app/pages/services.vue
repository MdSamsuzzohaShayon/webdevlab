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
            Our <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-secondary-600">Services</span>
          </h1>
          <p class="text-xl text-gray-600 mb-8 max-w-3xl mx-auto animate-slide-up">
            We provide cutting-edge solutions in web development, AI integration, Web3 technologies, and more. 
            Our expert team delivers scalable, high-performance applications tailored to your needs.
          </p>
        </div>
      </section>
  
      <!-- Services Grid -->
      <section class="relative py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div 
              v-for="(service, index) in services" 
              :key="service.title"
              class="card group p-6 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2"
              :class="index % 2 === 0 ? 'animate-slide-left' : 'animate-slide-right'"
              :style="`animation-delay: ${index * 0.1}s`"
              @mouseenter="activeService = index"
              @mouseleave="activeService = null"
            >
              <div class="relative mb-6">
                <div class="w-16 h-16 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300">
                  <svg class="w-8 h-8 text-white" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path :d="service.icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <div class="absolute -top-2 -right-2 w-6 h-6 bg-accent-500 rounded-full flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                  <svg class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M13 10V3L4 14h7v7l9-11h-7z" />
                  </svg>
                </div>
              </div>
              <h3 class="text-xl font-semibold text-gray-900 mb-3 group-hover:text-primary-600 transition-colors duration-200">
                {{ service.title }}
              </h3>
              <p class="text-gray-600 mb-4">{{ service.description }}</p>
              <ul class="space-y-2 mb-6">
                <li v-for="(feature, i) in service.features" :key="i" class="flex items-start">
                  <svg class="w-5 h-5 text-green-500 mt-0.5 mr-2 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                  <span class="text-gray-600 text-sm">{{ feature }}</span>
                </li>
              </ul>
              <button class="text-primary-600 font-medium flex items-center group-hover:text-primary-700 transition-colors duration-200">
                Learn more
                <svg class="w-4 h-4 ml-1 transform group-hover:translate-x-1 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Tech Stack Section -->
      <section class="py-16 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-12">
            <h2 class="text-3xl font-bold text-gray-900">Our Technology Stack</h2>
            <p class="text-gray-600 mt-4">We work with modern technologies to deliver exceptional results</p>
          </div>
  
          <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-8">
            <div v-for="tech in technologies" :key="tech.name" class="flex flex-col items-center p-4 group">
              <div class="w-16 h-16 mb-4 bg-white rounded-xl shadow-md flex items-center justify-center p-3 group-hover:shadow-lg transition-shadow duration-300">
                <svg class="w-10 h-10 text-gray-700" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path :d="tech.icon" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <span class="text-sm font-medium text-gray-700">{{ tech.name }}</span>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Process Section -->
      <section class="py-16 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-12">
            <h2 class="text-3xl font-bold text-gray-900">Our Development Process</h2>
            <p class="text-gray-600 mt-4">A structured approach to delivering exceptional results</p>
          </div>
  
          <div class="relative">
            <!-- Timeline line -->
            <div class="absolute left-1/2 transform -translate-x-1/2 h-full w-1 bg-gradient-to-b from-primary-400 to-secondary-400 hidden md:block"></div>
            
            <div class="space-y-12 md:space-y-0">
              <div v-for="(step, index) in process" :key="step.title" class="flex flex-col md:flex-row md:items-center">
                <div :class="['md:w-1/2', index % 2 === 0 ? 'md:pr-12 md:text-right' : 'md:pl-12 md:order-2']">
                  <div class="card p-6">
                    <div class="w-12 h-12 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-full flex items-center justify-center text-white font-bold text-lg mb-4 md:mx-auto md:absolute md:left-1/2 md:transform md:-translate-x-1/2">
                      {{ index + 1 }}
                    </div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ step.title }}</h3>
                    <p class="text-gray-600">{{ step.description }}</p>
                  </div>
                </div>
                <div :class="['md:w-1/2', index % 2 === 0 ? 'md:pl-12' : 'md:pr-12 md:order-1']">
                  <div class="h-48 bg-gradient-to-r from-primary-100 to-secondary-100 rounded-xl flex items-center justify-center p-6">
                    <svg class="w-16 h-16 text-primary-600" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path :d="step.icon" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
  
      <!-- CTA Section -->
      <section class="py-16 bg-gradient-to-r from-primary-600 to-secondary-600">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 class="text-3xl font-bold text-white mb-4">Ready to Start Your Project?</h2>
          <p class="text-primary-100 text-lg mb-8">
            Let's discuss how we can help you achieve your goals with our expert services.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <button class="btn-primary bg-white text-primary-600 hover:bg-gray-100 px-8 py-4">
              Get in Touch
            </button>
            <button class="btn-outline border-white text-white hover:bg-white hover:text-primary-600 px-8 py-4">
              View Our Work
            </button>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script setup>
  // Services data
  const services = [
    {
      title: "AI-Powered Web Development",
      description: "Intelligent web solutions that learn and adapt to user behavior.",
      icon: "M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z",
      features: [
        "Smart user experience personalization",
        "Predictive analytics integration",
        "Chatbots and virtual assistants",
        "AI-driven content recommendations"
      ]
    },
    {
      title: "Web3 & Blockchain Solutions",
      description: "Decentralized applications and smart contracts for the new web.",
      icon: "M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1",
      features: [
        "Smart contract development",
        "NFT marketplace creation",
        "DeFi application development",
        "Blockchain integration consulting"
      ]
    },
    {
      title: "Mobile Application Development",
      description: "Cross-platform mobile apps that deliver exceptional user experiences.",
      icon: "M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z",
      features: [
        "iOS and Android app development",
        "React Native cross-platform solutions",
        "Progressive Web Apps (PWAs)",
        "App store optimization and deployment"
      ]
    },
    {
      title: "Cloud Hosting & DevOps",
      description: "Scalable, secure cloud infrastructure with automated deployment.",
      icon: "M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01",
      features: [
        "AWS, Azure, and Google Cloud deployment",
        "CI/CD pipeline setup",
        "Containerization with Docker & Kubernetes",
        "24/7 monitoring and maintenance"
      ]
    },
    {
      title: "Backend Development",
      description: "Robust server-side solutions that power your applications.",
      icon: "M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4",
      features: [
        "RESTful and GraphQL API development",
        "Database design and optimization",
        "Microservices architecture",
        "Authentication and authorization systems"
      ]
    },
    {
      title: "Performance & Scaling",
      description: "Optimize and scale your applications for millions of users.",
      icon: "M13 10V3L4 14h7v7l9-11h-7z",
      features: [
        "Application performance optimization",
        "Load testing and capacity planning",
        "Database scaling strategies",
        "Content delivery network (CDN) setup"
      ]
    }
  ];
  
  // Technologies data
  const technologies = [
    { name: "React", icon: "M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" },
    { name: "Vue.js", icon: "M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01" },
    { name: "Node.js", icon: "M11 4a2 2 0 100-4 2 2 0 000 4zm-2 4a2 2 0 100-4 2 2 0 000 4zm-2 4a2 2 0 100-4 2 2 0 000 4zm-2 4a2 2 0 100-4 2 2 0 000 4zm16-12a2 2 0 100-4 2 2 0 000 4zm-2 4a2 2 0 100-4 2 2 0 000 4zm-2 4a2 2 0 100-4 2 2 0 000 4zm-2 4a2 2 0 100-4 2 2 0 000 4z" },
    { name: "Python", icon: "M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" },
    { name: "AWS", icon: "M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01" },
    { name: "Docker", icon: "M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m4 4h6a2 2 0 002-2v-4a2 2 0 00-2-2h-6a2 2 0 00-2 2v4a2 2 0 002 2z" }
  ];
  
  // Process data
  const process = [
    {
      title: "Discovery & Planning",
      description: "We begin by understanding your goals, target audience, and requirements to create a detailed project plan.",
      icon: "M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"
    },
    {
      title: "Design & Prototyping",
      description: "Our designers create intuitive user interfaces and experiences that align with your brand and user needs.",
      icon: "M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
    },
    {
      title: "Development",
      description: "Our developers bring your project to life using the latest technologies and best practices.",
      icon: "M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"
    },
    {
      title: "Testing & Quality Assurance",
      description: "We rigorously test your application to ensure it performs flawlessly across all devices and scenarios.",
      icon: "M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
    },
    {
      title: "Deployment & Launch",
      description: "We handle the deployment process and ensure a smooth launch of your application.",
      icon: "M13 10V3L4 14h7v7l9-11h-7z"
    },
    {
      title: "Maintenance & Support",
      description: "We provide ongoing support and maintenance to keep your application running smoothly.",
      icon: "M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
    }
  ];
  
  const activeService = ref(null);
  
  useHead({
    title: "Our Services - WebDevLab",
    meta: [
      {
        name: "description",
        content: "Explore our expert services in web development, AI integration, Web3 technologies, mobile apps, and more.",
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
  
  .animate-slide-left {
    animation: slideLeft 0.8s ease-out;
  }
  
  .animate-slide-right {
    animation: slideRight 0.8s ease-out;
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
  
  @keyframes slideLeft {
    from { 
      opacity: 0;
      transform: translateX(20px);
    }
    to { 
      opacity: 1;
      transform: translateX(0);
    }
  }
  
  @keyframes slideRight {
    from { 
      opacity: 0;
      transform: translateX(-20px);
    }
    to { 
      opacity: 1;
      transform: translateX(0);
    }
  }
  </style>