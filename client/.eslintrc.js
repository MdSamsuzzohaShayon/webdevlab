module.exports = {
  env: {
    browser: true,
    node: true,
  },
  extends: [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:vue/vue3-recommended",
  ],
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: "module",
    parser: "@typescript-eslint/parser",
  },
  plugins: ["@typescript-eslint", "vue"],
  rules: {
    "import/extensions": [
      "error",
      "always",
      {
          "pattern": {
              "ts": "never",
              "vue": "never",
          }
      }
  ],
    "no-unused-vars": "off",
    "@typescript-eslint/no-unused-vars": ["error"],
    "vue/no-unused-components": "off",
  },
  globals: {
    // Define global variables here
    // Example:
    // myGlobalVar: true,
  },
};
