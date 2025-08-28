<template>
    <div class="min-h-screen bg-gray-50">
      <AppHeader />
      <main>
        <slot />
      </main>
      <AppFooter />
      <ExternalLinkModal />
    </div>
  </template>
  
  <script setup>
  // Auto-append website URL when copying text
  onMounted(() => {
    document.addEventListener('copy', (e) => {
      const selection = document.getSelection()?.toString()
      if (selection && selection.length > 0) {
        const websiteUrl = '\n\nSource: ' + window.location.origin
        const modifiedText = selection + websiteUrl
        
        e.clipboardData?.setData('text/plain', modifiedText)
        e.preventDefault()
      }
    })
  })
  </script>