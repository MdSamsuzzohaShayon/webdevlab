<template>
  <div class="min-h-screen bg-gray-50 font-sans">
    <!-- Header -->
    <header class="bg-blue-600 text-white p-4 shadow-md">
      <h1 class="text-2xl font-bold">Web Dev Lab</h1>
    </header>

    <!-- Hero Section -->
    <section class="text-center py-16 bg-gradient-to-r from-blue-400 to-purple-500 text-white">
      <h2 class="text-3xl md:text-4xl font-bold mb-4">Welcome to Web Dev Lab</h2>
      <p class="text-lg md:text-xl">Experiment, Learn, and Build amazing Web Projects!</p>
      <button class="mt-6 px-6 py-2 bg-white text-blue-600 font-semibold rounded hover:bg-gray-100 transition">Get Started</button>
    </section>

    <!-- Cards Section -->
    <section class="py-12 px-4 md:px-16">
      <h3 class="text-2xl font-bold mb-6 text-center">Projects & Experiments</h3>
      <div class="grid gap-6 md:grid-cols-3">
        <div class="bg-white p-6 rounded-lg shadow hover:shadow-lg transition">
          <h4 class="font-semibold text-xl mb-2">Project 1</h4>
          <p class="text-gray-600">A small Vue.js experiment with interactive UI components.</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow hover:shadow-lg transition">
          <h4 class="font-semibold text-xl mb-2">Project 2</h4>
          <p class="text-gray-600">Exploring Tailwind CSS layouts and responsive design.</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow hover:shadow-lg transition">
          <h4 class="font-semibold text-xl mb-2">Project 3</h4>
          <p class="text-gray-600">Combining Vue.js with external APIs for real-time data.</p>
        </div>
      </div>
    </section>

    <div class="h-96"></div>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white p-4 text-center">
      &copy; 2025 Web Dev Lab. All rights reserved.
    </footer>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>
