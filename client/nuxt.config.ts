// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ["@nuxtjs/apollo"],
  apollo: {
    clients: {
      default: {
        httpEndpoint: "http://localhost:8000/graphql/",
        httpLinkOptions: { credentials: "include" },
      },
    },
  },
});