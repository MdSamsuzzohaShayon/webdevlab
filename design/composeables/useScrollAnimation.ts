export default function useScrollAnimation() {
    const observeElements = () => {
      if (process.client) {
        const observer = new IntersectionObserver(
          (entries) => {
            entries.forEach((entry) => {
              if (entry.isIntersecting) {
                entry.target.classList.add('in-view')
              }
            })
          },
          {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
          }
        )
  
        // Observe all elements with animate-on-scroll class
        const elements = document.querySelectorAll('.animate-on-scroll')
        elements.forEach((el) => observer.observe(el))
  
        return observer
      }
    }
  
    return {
      observeElements
    }
  }