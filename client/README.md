# Nuxt js blog

 - Add article with thumbnail image
 - Display article content properly according to quill editor


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