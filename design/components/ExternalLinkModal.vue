<template>
    <div v-if="showModal" class="fixed inset-0 z-50 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
      <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <!-- Background overlay -->
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true" @click="closeModal"></div>
  
        <!-- Modal panel -->
        <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <div class="sm:flex sm:items-start">
              <div class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                <svg class="h-6 w-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
              </div>
              <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left w-full">
                <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                  You're leaving WebDevLab
                </h3>
                <div class="mt-2">
                  <p class="text-sm text-gray-500 mb-4">
                    You're about to visit an external link. Stay connected with us for more amazing content!
                  </p>
                  
                  <form @submit.prevent="handleSubmit" class="space-y-4">
                    <div>
                      <label for="email" class="block text-sm font-medium text-gray-700">Email address</label>
                      <input
                        v-model="email"
                        type="email"
                        id="email"
                        required
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                        placeholder="Enter your email"
                      >
                    </div>
                    
                    <div class="flex items-center">
                      <input
                        v-model="agreeToEmails"
                        id="agree-emails"
                        type="checkbox"
                        required
                        class="h-4 w-4 text-primary-600 focus:ring-primary-500 border-gray-300 rounded"
                      >
                      <label for="agree-emails" class="ml-2 block text-sm text-gray-900">
                        I agree to receive emails from this website
                      </label>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
            <button
              @click="handleSubmit"
              type="button"
              class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-primary-600 text-base font-medium text-white hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 sm:ml-3 sm:w-auto sm:text-sm"
            >
              Continue to External Site
            </button>
            <button
              @click="closeModal"
              type="button"
              class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm"
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  const showModal = ref(false)
  const email = ref('')
  const agreeToEmails = ref(false)
  const pendingUrl = ref('')
  
  const openModal = (url) => {
    pendingUrl.value = url
    showModal.value = true
  }
  
  const closeModal = () => {
    showModal.value = false
    email.value = ''
    agreeToEmails.value = false
    pendingUrl.value = ''
  }
  
  const handleSubmit = () => {
    if (email.value && agreeToEmails.value) {
      // Here you would typically save the email to your database
      console.log('Email submitted:', email.value)
      
      // Open the external link
      window.open(pendingUrl.value, '_blank')
      closeModal()
    }
  }
  
  // Global function to handle external links
  if (process.client) {
    window.openExternalLink = (url) => {
      openModal(url)
    }
  }
  
  // Listen for external link clicks
  onMounted(() => {
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a')
      if (link && link.href && (link.href.includes('github.com') || link.href.includes('external'))) {
        e.preventDefault()
        openModal(link.href)
      }
    })
  })
  </script>