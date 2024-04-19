// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  devtools: { enabled: true },
  app: {
    // <link href="https://cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet">
    head: {
      // link: [{ rel: "stylesheet", href: "https://cdn.quilljs.com/1.3.6/quill.snow.css" }],
    },
    pageTransition: {
      name: 'fade',
      mode: 'out-in', // default
    },
    layoutTransition: {
      name: 'slide',
      mode: 'out-in', // default
    },
  },
  components: [
    {
      path: '~/components/layouts',
      pathPrefix: false,
      extensions: ['.vue'],
    },
    {
      path: '~/components/home',
      pathPrefix: false,
      extensions: ['.vue'],
    },
    {
      path: '~/components/admin',
      pathPrefix: false,
      extensions: ['.vue'],
    },
    {
      path: '~/components/article',
      pathPrefix: false,
      extensions: ['.vue'],
    },
    {
      path: '~/components/category',
      pathPrefix: false,
      extensions: ['.vue'],
    },
    {
      path: '~/components/author',
      pathPrefix: false,
      extensions: ['.vue'],
    },
    {
      path: '~/components/elements',
      pathPrefix: false,
      extensions: ['.vue'],
    },
    // "~/components",
  ],
  typescript: {
    strict: true,
  },
  modules: [
    '@nuxtjs/apollo',
    '@nuxt/devtools',
    '@nuxtjs/cloudinary',
    'nuxt-icon',
    '@nuxtjs/eslint-module',
  ],
  // buildModules: ['@nuxt/typescript-build'],
  apollo: {
    autoImports: true,
    clients: {
      default: {
        httpEndpoint: 'http://localhost:8000/graphql/',
      },
    },
  },
  plugins: [
    // '~/plugins/apollo-client.ts'
    { src: '~/plugins/bootstrap-client.ts', mode: 'client' }
  ],
  // some nuxt config...
  css: [
    'bootstrap/dist/css/bootstrap.min.css',
    // ...
    'quill/dist/quill.core.css',
    // for snow theme
    'quill/dist/quill.snow.css',
    // for bubble theme
    'quill/dist/quill.bubble.css',
    // ...
  ],
});
