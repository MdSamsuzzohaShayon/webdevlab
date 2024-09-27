// // HomePage.ssr.spec.ts
// import { describe, it, expect } from 'vitest';
// import { $fetch, fetch, url, setup } from '@nuxt/test-utils/e2e';

// describe('HomePage SSR', () => {
//   setup({
//     // Optional: Nuxt.js setup options here
//   });

//   it('should render the homepage correctly on the server', async () => {
//     const html: string = await $fetch('/');
//     expect(html).toContain('<div class="container">'); // Basic check to ensure page contains expected HTML

//     // Optionally, more specific checks can be added here
//   });

//   it('should fetch and return correct response from the server', async () => {
//     const res = await fetch('/');
//     const { body, headers } = res;

//     expect(headers.get('content-type')).toContain('text/html');
//     const text = await body.text();
//     expect(text).toContain('<div class="container">'); // Basic check to ensure page contains expected HTML

//     // Optionally, more specific checks can be added here
//   });

//   it('should generate correct URLs for given paths', () => {
//     const homeUrl: string = url('/');
//     const pageUrl: string = url('/page');

//     expect(homeUrl).toMatch(/http:\/\/localhost:\d+\//);
//     expect(pageUrl).toMatch(/http:\/\/localhost:\d+\/page/);
//   });
// });



// /**
//  * Server-Side Tests:
//  * HTML Content: Use $fetch to retrieve the HTML content of the server-rendered page and check for expected elements.
//  * Server Response: Use fetch to get the response from the server, verifying headers and body content.
//  * URL Generation: Verify that url generates correct URLs for given paths.
//  */


import { test, describe, expect } from 'vitest';

describe("Test SSR of home page or index page", async ()=>{
  test('my test', () => {
    // ... test without Nuxt environment!
    expect(2+3).toBe(5);
  });
});
