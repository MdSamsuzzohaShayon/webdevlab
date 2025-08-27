<template>
    <div class="min-h-screen bg-gray-50">
      <!-- Hero Section -->
      <section class="bg-white py-16 border-b border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center">
            <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
              Career Portal
            </h1>
            <p class="text-xl text-gray-600 max-w-3xl mx-auto">
              Find your dream job and advance your career with our exclusive opportunities from top tech companies.
            </p>
          </div>
        </div>
      </section>
  
      <!-- Job Listings -->
      <section class="py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <!-- Filters -->
          <div class="bg-white rounded-lg shadow-sm p-6 mb-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Location</label>
                <select class="w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500">
                  <option>All Locations</option>
                  <option>Remote</option>
                  <option>New York</option>
                  <option>San Francisco</option>
                  <option>London</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Experience</label>
                <select class="w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500">
                  <option>All Levels</option>
                  <option>Entry Level</option>
                  <option>Mid Level</option>
                  <option>Senior Level</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Job Type</label>
                <select class="w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500">
                  <option>All Types</option>
                  <option>Full-time</option>
                  <option>Part-time</option>
                  <option>Contract</option>
                </select>
              </div>
              <div class="flex items-end">
                <button class="btn-primary w-full">
                  Search Jobs
                </button>
              </div>
            </div>
          </div>
  
          <!-- Job Cards -->
          <div class="space-y-6">
            <div 
              v-for="job in jobs" 
              :key="job.id"
              class="card p-6 hover:shadow-xl transition-all duration-300"
            >
              <div class="flex items-start justify-between">
                <div class="flex items-start space-x-4">
                  <img 
                    :src="job.company.logo" 
                    :alt="job.company.name"
                    class="w-12 h-12 rounded-lg"
                  >
                  <div class="flex-1">
                    <h3 class="text-xl font-bold text-gray-900 mb-2">{{ job.title }}</h3>
                    <p class="text-gray-600 mb-2">{{ job.company.name }}</p>
                    <div class="flex flex-wrap gap-4 text-sm text-gray-500 mb-4">
                      <span class="flex items-center">
                        <svg class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                        </svg>
                        {{ job.location }}
                      </span>
                      <span class="flex items-center">
                        <svg class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        {{ job.type }}
                      </span>
                      <span class="flex items-center">
                        <svg class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1" />
                        </svg>
                        {{ job.salary }}
                      </span>
                    </div>
                    <p class="text-gray-700 mb-4">{{ job.description }}</p>
                    <div class="flex flex-wrap gap-2 mb-4">
                      <span 
                        v-for="skill in job.skills" 
                        :key="skill"
                        class="px-3 py-1 bg-primary-100 text-primary-800 text-sm rounded-full"
                      >
                        {{ skill }}
                      </span>
                    </div>
                  </div>
                </div>
                <div class="text-right">
                  <p class="text-sm text-gray-500 mb-4">Posted {{ job.postedDate }}</p>
                  <button class="btn-primary">
                    Apply Now
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
    title: 'Career - WebDevLab',
    meta: [
      { name: 'description', content: 'Find your dream job in web development with our career portal.' }
    ]
  })
  
  const jobs = [
    {
      id: 1,
      title: 'Senior Frontend Developer',
      company: {
        name: 'TechCorp Inc.',
        logo: 'https://images.pexels.com/photos/270348/pexels-photo-270348.jpeg?w=100&h=100&fit=crop'
      },
      location: 'Remote',
      type: 'Full-time',
      salary: '$120k - $150k',
      description: 'We are looking for a Senior Frontend Developer to join our growing team and help build amazing user experiences.',
      skills: ['React', 'TypeScript', 'Next.js', 'Tailwind CSS'],
      postedDate: '2 days ago'
    },
    {
      id: 2,
      title: 'Full Stack JavaScript Developer',
      company: {
        name: 'StartupXYZ',
        logo: 'https://images.pexels.com/photos/574071/pexels-photo-574071.jpeg?w=100&h=100&fit=crop'
      },
      location: 'San Francisco, CA',
      type: 'Full-time',
      salary: '$100k - $130k',
      description: 'Join our innovative startup and work on cutting-edge web applications using modern JavaScript technologies.',
      skills: ['Node.js', 'Vue.js', 'MongoDB', 'Express'],
      postedDate: '1 week ago'
    },
    {
      id: 3,
      title: 'React Native Mobile Developer',
      company: {
        name: 'Mobile Solutions',
        logo: 'https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg?w=100&h=100&fit=crop'
      },
      location: 'New York, NY',
      type: 'Contract',
      salary: '$80 - $100/hr',
      description: 'Develop cross-platform mobile applications using React Native for our diverse client base.',
      skills: ['React Native', 'JavaScript', 'iOS', 'Android'],
      postedDate: '3 days ago'
    }
  ]
  </script>