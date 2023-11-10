// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  components: [
    {
      path: "~/components/layouts",
      pathPrefix: false,
      extensions: ['.vue'],
    },
    {
      path: "~/components/home",
      pathPrefix: false,
      extensions: ['.vue'],
    },
    {
      path: "~/components/admin",
      pathPrefix: false,
      extensions: ['.vue'],
    },
    {
      path: "~/components/article",
      pathPrefix: false,
      extensions: ['.vue'],
    },
    "~/components",
  ],
  typescript: {
    strict: true,
  },
  modules: ["@nuxtjs/apollo", "@nuxtjs/tailwindcss", "@nuxt/devtools"],
  apollo: {
    clients: {
      default: {
        httpEndpoint: "http://localhost:8000/graphql/",
        httpLinkOptions: { credentials: "include" },
      },
    },
  },
});
