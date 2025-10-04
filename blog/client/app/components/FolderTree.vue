<template>
    <div class="space-y-1">
      <div 
        v-for="(item, index) in structure.children" 
        :key="item.name"
        class="folder-item group"
      >
        <!-- Root Level -->
        <div class="flex items-center py-2 px-3 rounded-lg hover:bg-white/50 dark:hover:bg-slate-800/50 transition-all duration-200">
          <!-- Folder/File Icon -->
          <div class="w-6 h-6 flex items-center justify-center mr-3">
            <svg 
              v-if="item.type === 'folder'" 
              class="w-4 h-4 text-[#D6E74E] group-hover:text-[#20D9C4] transition-colors duration-200" 
              fill="currentColor" 
              viewBox="0 0 20 20"
            >
              <path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"/>
            </svg>
            <svg 
              v-else 
              class="w-4 h-4 text-[#3366FF] group-hover:text-[#8A2BE2] transition-colors duration-200" 
              fill="currentColor" 
              viewBox="0 0 20 20"
            >
              <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z" clip-rule="evenodd"/>
            </svg>
          </div>
          
          <!-- Name with gradient text effect -->
          <span class="text-slate-700 dark:text-slate-300 font-medium group-hover:text-[#8A2BE2] dark:group-hover:text-[#20D9C4] transition-colors duration-200">
            {{ item.name }}
          </span>
          
          <!-- File type badge -->
          <span 
            v-if="item.type === 'file'"
            class="ml-2 px-2 py-1 text-xs bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-400 rounded-md font-mono"
          >
            {{ getFileExtension(item.name) }}
          </span>
        </div>
  
        <!-- Nested Children with beautiful indentation -->
        <div 
          v-if="item.children && item.children.length > 0" 
          class="ml-6 border-l-2 border-slate-200 dark:border-slate-700 pl-4 space-y-1"
        >
          <FolderTree :structure="item" />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    structure: {
      type: Object,
      required: true
    }
  })
  
  // Helper function to get file extension
  const getFileExtension = (filename) => {
    return filename.split('.').pop() || 'file'
  }
  </script>
  
  <style scoped>
  .folder-item {
    position: relative;
  }
  
  .folder-item::before {
    content: '';
    position: absolute;
    left: -12px;
    top: 50%;
    width: 8px;
    height: 8px;
    background: linear-gradient(135deg, #8A2BE2, #3366FF);
    border-radius: 50%;
    transform: translateY(-50%);
    opacity: 0;
    transition: opacity 0.3s ease;
  }
  
  .folder-item:hover::before {
    opacity: 1;
  }
  
  /* Smooth animation for nested items */
  .folder-item > div {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }
  
  .folder-item:hover > div {
    transform: translateX(4px);
  }
  </style>