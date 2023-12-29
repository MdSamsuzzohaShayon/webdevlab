// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  app: {
    // <link href="https://cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet">
    head: {
      // link: [{ rel: "stylesheet", href: "https://cdn.quilljs.com/1.3.6/quill.snow.css" }],
    },
  },
  components: [
    {
      path: "~/components/layouts",
      pathPrefix: false,
      extensions: [".vue"],
    },
    {
      path: "~/components/home",
      pathPrefix: false,
      extensions: [".vue"],
    },
    {
      path: "~/components/admin",
      pathPrefix: false,
      extensions: [".vue"],
    },
    {
      path: "~/components/article",
      pathPrefix: false,
      extensions: [".vue"],
    },
    {
      path: "~/components/category",
      pathPrefix: false,
      extensions: [".vue"],
    },
    {
      path: "~/components/author",
      pathPrefix: false,
      extensions: [".vue"],
    },
    {
      path: "~/components/elements",
      pathPrefix: false,
      extensions: [".vue"],
    },
    // "~/components",
  ],
  typescript: {
    strict: true,
  },
  modules: ["@nuxtjs/apollo", "@nuxtjs/tailwindcss", "@nuxt/devtools", "@nuxtjs/cloudinary"],
  apollo: {
    clients: {
      default: {
        httpEndpoint: "http://localhost:8000/graphql/",
        // httpLinkOptions: { credentials: "include" },
      },
    },
  },
  plugins: [],
  // some nuxt config...
  css: [
    // ...
    "quill/dist/quill.core.css",
    // for snow theme
    "quill/dist/quill.snow.css",
    // for bubble theme
    "quill/dist/quill.bubble.css",
    // ...
  ],
});
