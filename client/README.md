# Nuxt js blog

 - Add article with thumbnail image
 - Display article content properly according to quill editor


# Requirements
 - Create a post with multiple categories
 - Make it more responsive
 - Categories are tutorial, news,

 # Testing Guide for Nuxt.js Frontend Applications

## 1. Component Tests

- **Unit Testing Components**:
  - Test individual Vue components for correct rendering and behavior.
  - Use tools like Jest or Vue Test Utils for unit testing.

- **Props Validation**:
  - Verify that components receive and handle props correctly.

- **Event Handling**:
  - Test event handlers and ensure they trigger the expected behavior.

## 2. Pages and Routes

- **Route Navigation**:
  - Test page navigation and ensure routing works correctly.

- **Page Rendering**:
  - Validate that each page renders the expected content and components.

## 3. API and Data Fetching

- **Mocking API Calls**:
  - Use `axios-mock-adapter` to mock API responses and test data fetching logic.

- **Testing Vuex Store**:
  - Validate Vuex store actions, mutations, and state changes related to data fetching.

## 4. Vuex State Management

- **State Mutation**:
  - Test Vuex mutations to ensure state changes are applied correctly.

- **Action Dispatching**:
  - Verify that Vuex actions trigger the intended mutations and API calls.

## 5. Integration Tests

- **Testing Page Interactions**:
  - Test interactions between multiple components/pages.

- **Testing Layouts and Middleware**:
  - Validate how layouts and middleware affect page rendering and behavior.

## 6. User Interface (UI) and User Experience (UX)

- **Functional Testing**:
  - Use Cypress or Selenium for end-to-end testing to simulate user interactions.

- **Accessibility Testing**:
  - Ensure the application is accessible to users with disabilities.

## 7. Performance and Optimization

- **Performance Testing**:
  - Use Lighthouse or WebPageTest to measure and optimize performance metrics.

## 8. Error Handling

- **Testing Error States**:
  - Verify how the application handles different types of errors.

## 9. Cross-Browser and Cross-Device Testing

- **Browser Compatibility**:
  - Test the application across different browsers and devices.

## 10. Security Testing

- **Testing Authentication and Authorization**:
  - Validate how the application handles user authentication and authorization.

## 11. Localization and Internationalization (i18n)

- **Testing Translations**:
  - Ensure text translations and internationalization features work correctly.

## 12. Usability Testing

- **User Workflow Testing**:
  - Validate common user workflows to ensure the application is user-friendly.

### Tools and Libraries:

- **Testing Frameworks**:
  - Jest, Mocha for unit and integration testing.
  - Vue Test Utils for testing Vue components.
  - Cypress or Selenium WebDriver for end-to-end testing.

- **Additional Libraries**:
  - axios-mock-adapter for mocking API requests.
  - Vuex Test Utils for testing Vuex store.
  - Lighthouse or WebPageTest for performance testing.

---

By covering these areas in your testing strategy, you can ensure that your Nuxt.js frontend application is robust, reliable, and delivers a great user experience across different scenarios and environments.

# Design
 - Main theme design inspired by https://networkertheme.com/networker/
 - Dashboard design inspiration - https://aries-admin-templates.websitedesignmarketingagency.com/ariesadmin-dark/ser/

### Testing document
 - [How to test nuxt composable useAsyncData in vitest #2205](https://github.com/vitest-dev/vitest/discussions/2205)
 - [End to end and unit testing](https://github.com/vinayakkulkarni/nuxt-ava-e2e-unit-testing/blob/main/test/_setup.js)


### End-to-end testing

 - **End-to-End Testing (E2E):**
 - End-to-end tests in Nuxt.js with Vitest typically involve testing the entire application from the user's perspective, including interactions with different pages and components. Vitest offers E2E testing capabilities through the use of testing libraries such as @vue/test-utils and @testing-library/*.
 - Example (Vitest E2E with @testing-library/vue): Suppose you have a Nuxt.js application with a simple login page. You want to write an end-to-end test to ensure that users can successfully log in.
  ```
  // e2e/login.spec.js

    import { createTest, vue } from 'vitest';
    import Login from '~/pages/login.vue';
    import { render, fireEvent } from '@testing-library/vue';

    createTest('Login Page', () => {
      it('successfully logs in with correct credentials', async () => {
        const { getByLabelText, getByText } = render(Login, { vue });
        const usernameInput = getByLabelText('Username');
        const passwordInput = getByLabelText('Password');

        await fireEvent.update(usernameInput, 'example_user');
        await fireEvent.update(passwordInput, 'password123');

        const submitButton = getByText('Login');
        await fireEvent.click(submitButton);

        // Assert redirection or success message
      });

      it('displays error message with incorrect credentials', async () => {
        const { getByLabelText, getByText } = render(Login, { vue });
        const usernameInput = getByLabelText('Username');
        const passwordInput = getByLabelText('Password');

        await fireEvent.update(usernameInput, 'wrong_user');
        await fireEvent.update(passwordInput, 'wrong_password');

        const submitButton = getByText('Login');
        await fireEvent.click(submitButton);

        // Assert error message
      });
    });

  ```
 - **Unit Testing:**
 - Unit testing in Nuxt.js with Vitest focuses on testing individual units of code, such as components, functions, or modules, in isolation. Vitest provides utilities for unit testing Vue components and other JavaScript modules.
 - Example (Vitest Unit Test): Suppose you have a simple Vue component that displays a greeting message.
  ```
    <!-- components/Greeting.vue -->
    <template>
      <div>
        <h1>{{ greeting }}</h1>
      </div>
    </template>

    <script>
    export default {
      props: {
        name: {
          type: String,
          required: true
        }
      },
      computed: {
        greeting() {
          return `Hello, ${this.name}!`;
        }
      }
    };
    </script>
  ```