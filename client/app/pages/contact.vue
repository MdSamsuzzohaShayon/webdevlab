<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
    <!-- Hero Section -->
    <section class="relative overflow-hidden py-20 sm:py-32">
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

      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1
          class="text-4xl sm:text-6xl font-bold text-gray-900 mb-6 animate-fade-in"
        >
          Get in
          <span
            class="text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-secondary-600"
            >Touch</span
          >
        </h1>
        <p
          class="text-xl text-gray-600 mb-8 max-w-3xl mx-auto animate-slide-up"
        >
          Have questions or want to discuss a project? We'd love to hear from
          you. Reach out to us through any of the channels below or send us a
          message.
        </p>
      </div>
    </section>

    <!-- Contact Content -->
    <section class="relative py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
          <!-- Contact Information -->
          <div class="space-y-8 animate-slide-left">
            <div>
              <h2 class="text-3xl font-bold text-gray-900 mb-6">
                Contact Information
              </h2>
              <p class="text-gray-600 mb-8">
                Feel free to reach out to us for any inquiries, collaborations,
                or just to say hello. We're always excited to connect with
                fellow learners and creators.
              </p>
            </div>

            <!-- Contact Methods -->
            <div class="space-y-6">
              <div
                v-for="(method, index) in contactMethods"
                :key="method.title"
                class="flex items-start p-6 rounded-xl bg-white shadow-md hover:shadow-lg transition-all duration-300 group"
                :class="
                  index % 2 === 0 ? 'animate-slide-left' : 'animate-slide-right'
                "
                :style="`animation-delay: ${index * 0.1}s`"
              >
                <div
                  class="flex-shrink-0 w-12 h-12 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-lg flex items-center justify-center mr-4 group-hover:scale-110 transition-transform duration-300"
                >
                  <svg
                    class="w-6 h-6 text-white"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      :d="method.icon"
                    />
                  </svg>
                </div>
                <div>
                  <h3 class="text-lg font-semibold text-gray-900 mb-1">
                    {{ method.title }}
                  </h3>
                  <p class="text-gray-600 mb-2">{{ method.value }}</p>
                  <a
                    :href="method.link"
                    class="text-primary-600 font-medium inline-flex items-center hover:text-primary-700 transition-colors duration-200"
                  >
                    {{ method.action }}
                    <svg
                      class="w-4 h-4 ml-1"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M14 5l7 7m0 0l-7 7m7-7H3"
                      />
                    </svg>
                  </a>
                </div>
              </div>
            </div>

            <!-- Social Links -->
            <div class="pt-8">
              <h3 class="text-xl font-semibold text-gray-900 mb-4">
                Follow Us
              </h3>
              <div class="flex space-x-4">
                <a
                  v-for="social in socialLinks"
                  :key="social.name"
                  :href="social.link"
                  class="w-12 h-12 bg-white rounded-lg shadow-md flex items-center justify-center text-gray-700 hover:bg-primary-50 hover:text-primary-600 transition-all duration-300 transform hover:-translate-y-1"
                  :aria-label="social.name"
                >
                  <svg
                    class="w-6 h-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      :d="social.icon"
                    />
                  </svg>
                </a>
              </div>
            </div>
          </div>

          <!-- Contact Form -->
          <div class="card p-8 animate-slide-right">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">
              Send us a Message
            </h2>
            <form @submit.prevent="handleSubmit" class="space-y-6">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                <div>
                  <label
                    for="name"
                    class="block text-sm font-medium text-gray-700 mb-1"
                    >Your Name</label
                  >
                  <input
                    type="text"
                    id="name"
                    v-model="formData.name"
                    required
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-colors duration-200"
                    placeholder="Enter your name"
                  />
                </div>
                <div>
                  <label
                    for="email"
                    class="block text-sm font-medium text-gray-700 mb-1"
                    >Email Address</label
                  >
                  <input
                    type="email"
                    id="email"
                    v-model="formData.email"
                    required
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-colors duration-200"
                    placeholder="your.email@example.com"
                  />
                </div>
              </div>
              <div>
                <label
                  for="subject"
                  class="block text-sm font-medium text-gray-700 mb-1"
                  >Subject</label
                >
                <input
                  type="text"
                  id="subject"
                  v-model="formData.subject"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-colors duration-200"
                  placeholder="What is this regarding?"
                />
              </div>
              <div>
                <label
                  for="message"
                  class="block text-sm font-medium text-gray-700 mb-1"
                  >Your Message</label
                >
                <textarea
                  id="message"
                  v-model="formData.message"
                  required
                  rows="5"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-colors duration-200"
                  placeholder="Tell us how we can help you..."
                ></textarea>
              </div>
              <button
                type="submit"
                class="w-full btn-primary py-4 text-lg flex items-center justify-center"
                :disabled="isSubmitting"
              >
                <span v-if="!isSubmitting">Send Message</span>
                <span v-else class="flex items-center">
                  <svg
                    class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                  >
                    <circle
                      class="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      stroke-width="4"
                    ></circle>
                    <path
                      class="opacity-75"
                      fill="currentColor"
                      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                    ></path>
                  </svg>
                  Sending...
                </span>
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>

    <!-- Map Section -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-900">Our Location</h2>
          <p class="text-gray-600 mt-4">
            Come visit us at our office in Dhaka, Bangladesh
          </p>
        </div>

        <div
          class="bg-gradient-to-br from-primary-50 to-secondary-50 rounded-2xl overflow-hidden shadow-xl p-8"
        >
          <div class="flex flex-col lg:flex-row gap-8">
            <div
              class="lg:w-2/3 h-96 bg-gray-200 rounded-xl overflow-hidden relative"
            >
              <!-- Map placeholder with interactive elements -->
              <div
                class="absolute inset-0 bg-gradient-to-br from-primary-100 to-secondary-100 flex items-center justify-center"
              >
                <svg
                  class="w-24 h-24 text-primary-600 opacity-50"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="1"
                    d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="1"
                    d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                </svg>

                <!-- Interactive markers -->
                <div
                  class="absolute top-1/2 left-1/2 w-4 h-4 bg-primary-600 rounded-full transform -translate-x-1/2 -translate-y-1/2 animate-ping"
                ></div>
                <div
                  class="absolute top-1/2 left-1/2 w-6 h-6 bg-primary-500 rounded-full transform -translate-x-1/2 -translate-y-1/2 flex items-center justify-center"
                >
                  <div class="w-2 h-2 bg-white rounded-full"></div>
                </div>

                <!-- Location text that appears on hover -->
                <div
                  class="absolute bottom-4 left-4 bg-white/90 backdrop-blur-sm px-4 py-2 rounded-lg shadow-md opacity-0 hover:opacity-100 transition-opacity duration-300"
                >
                  <p class="text-sm font-medium text-gray-900">
                    58-gha-4, West Raaja Bazaar
                  </p>
                  <p class="text-xs text-gray-600">Dhaka, Bangladesh</p>
                </div>
              </div>
            </div>

            <div class="lg:w-1/3 space-y-6">
              <div class="bg-white p-6 rounded-xl shadow-sm">
                <h3 class="text-xl font-semibold text-gray-900 mb-4">
                  Visit Our Office
                </h3>
                <p class="text-gray-600 mb-4">
                  We're located in the heart of Dhaka. Feel free to stop by
                  during business hours.
                </p>
                <div class="space-y-3">
                  <div class="flex items-start">
                    <svg
                      class="w-5 h-5 text-primary-600 mt-0.5 mr-3 flex-shrink-0"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                      />
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                      />
                    </svg>
                    <span class="text-gray-600"
                      >58-gha-4, West Raaja Bazaar, Dhaka, Bangladesh</span
                    >
                  </div>
                  <div class="flex items-start">
                    <svg
                      class="w-5 h-5 text-primary-600 mt-0.5 mr-3 flex-shrink-0"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                      />
                    </svg>
                    <span class="text-gray-600"
                      >Monday - Friday: 9AM - 5PM<br />Saturday: 10AM -
                      3PM</span
                    >
                  </div>
                </div>
              </div>

              <button
                class="w-full btn-outline flex items-center justify-center"
              >
                <svg
                  class="w-5 h-5 mr-2"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"
                  />
                </svg>
                Get Directions
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="py-16 bg-gray-50">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-900">
            Frequently Asked Questions
          </h2>
          <p class="text-gray-600 mt-4">Quick answers to common questions</p>
        </div>

        <div class="space-y-4">
          <div
            v-for="(faq, index) in faqs"
            :key="faq.question"
            class="card p-6 transition-all duration-300"
            :class="{ 'bg-primary-50': activeFaq === index }"
            @click="activeFaq = activeFaq === index ? null : index"
          >
            <button class="flex items-center justify-between w-full text-left">
              <h3 class="text-lg font-medium text-gray-900">
                {{ faq.question }}
              </h3>
              <svg
                class="w-5 h-5 text-gray-500 transform transition-transform duration-300"
                :class="{ 'rotate-180': activeFaq === index }"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 9l-7 7-7-7"
                />
              </svg>
            </button>
            <div
              class="mt-4 text-gray-600 overflow-hidden transition-all duration-300"
              :class="activeFaq === index ? 'max-h-96' : 'max-h-0'"
            >
              {{ faq.answer }}
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
// Contact methods data
const contactMethods = [
  {
    title: "Email Us",
    value: "admin@email.com",
    icon: "M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z",
    link: "mailto:admin@email.com",
    action: "Send an email",
  },
  {
    title: "Call Us",
    value: "+8801889171929",
    icon: "M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z",
    link: "tel:+8801889171929",
    action: "Call now",
  },
  {
    title: "Visit Us",
    value: "58-gha-4, West Raaja Bazaar, Dhaka, Bangladesh",
    icon: "M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z M15 11a3 3 0 11-6 0 3 3 0 016 0z",
    link: "https://maps.google.com/?q=58-gha-4,West+Raaja+Bazaar,Dhaka,Bangladesh",
    action: "Get directions",
  },
];

// Social links data
const socialLinks = [
  {
    name: "Twitter",
    link: "#",
    icon: "M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z",
  },
  {
    name: "LinkedIn",
    link: "#",
    icon: "M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6z M2 9h4v12H2z M4 6a2 2 0 100-4 2 2 0 000 4z",
  },
  {
    name: "Facebook",
    link: "#",
    icon: "M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z",
  },
  {
    name: "Instagram",
    link: "#",
    icon: "M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z",
  },
];

// FAQ data
const faqs = [
  {
    question: "What are your response times for emails?",
    answer:
      "We typically respond to all emails within 24 hours on business days. For urgent matters, we recommend calling us directly.",
  },
  {
    question: "Do you offer remote consultations?",
    answer:
      "Yes, we offer remote consultations via video call for clients who cannot visit our office in person. Please schedule an appointment in advance.",
  },
  {
    question: "What are your business hours?",
    answer:
      "Our standard business hours are Monday to Friday from 9:00 AM to 5:00 PM and Saturdays from 10:00 AM to 3:00 PM. We are closed on Sundays and public holidays.",
  },
  {
    question: "How can I schedule a meeting?",
    answer:
      "You can schedule a meeting by calling us, sending an email, or using our online booking system. We'll confirm your appointment within 24 hours.",
  },
];

// Form data
const formData = ref({
  name: "",
  email: "",
  subject: "",
  message: "",
});

const isSubmitting = ref(false);
const activeFaq = ref(null);

const handleSubmit = () => {
  isSubmitting.value = true;
  // Simulate form submission
  setTimeout(() => {
    alert("Thank you for your message! We'll get back to you soon.");
    formData.value = { name: "", email: "", subject: "", message: "" };
    isSubmitting.value = false;
  }, 1500);
};

useHead({
  title: "Contact Us - WebDevLab",
  meta: [
    {
      name: "description",
      content:
        "Get in touch with WebDevLab. Contact us via phone, email, or visit our office in Dhaka, Bangladesh.",
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
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
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
