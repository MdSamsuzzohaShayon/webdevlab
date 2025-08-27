// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  nitro: {
    output: {
      publicDir: 'dist'
    }
  },
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true }
});
