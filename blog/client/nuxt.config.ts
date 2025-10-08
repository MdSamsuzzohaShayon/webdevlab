// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  app: {
    head: {
      script: [
        {
          innerHTML: `(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
          new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
          j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
          'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
          })(window,document,'script','dataLayer','GTM-KXZ78V3V');`,
          type: "text/javascript",
          tagPosition: "head",
        },
      ],
      noscript: [
        {
          innerHTML: `<iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KXZ78V3V"
          height="0" width="0" style="display:none;visibility:hidden"></iframe>`,
          tagPosition: "bodyOpen",
        },
      ],
    },
  },

  devServer: {
    port: 3001, // default 3000
    // host: '0.0.0.0' // optional, useful for Docker/VPS
  },
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  modules: ["@nuxtjs/tailwindcss", "@nuxt/image"],
  css: [
    "~/assets/scss/main.scss",
    // 'swiper/css' // Updated path for Swiper v8+
  ],
  plugins: [{ src: "~/plugins/particles.js", mode: "client" }],
  build: {
    transpile: ["swiper"], // Add this to transpile Swiper
  },
});
