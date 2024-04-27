# Backend
 - Register user mutation
```
mutation RegisterUser($email: String!, $password: String!,
  $firstName: String!, $lastName: String!, $birth: String){
  registerUser(email: $email, password: $password,
    firstName: $firstName, lastName: $lastName, birth: $birth){
    user{
      id
      password
      lastLogin
      firstName
      lastName
      birth
    }
  }
}
```

```
{
  "email": "u2@example.com",
  "password": "Test1234",
  "firstName": "fn2",
  "lastName": "ln2",
  "birth": "2024-03-08T08:14:45.562Z"
}
```

- Verify User
```
mutation VerifyMutation($token: String!){
  verifyUser(token: $token){
    success
  }
}
```

```
{
  "token": "A_TOKEN"
}
```

- Login User

```
mutation Login($email: String! $password: String!){
  login(email: $email, password: $password){
    user{
      id
      lastLogin
      isActive
      firstName
      lastName
      email
    }
    accessToken
    refreshToken
  }
}
```

```
{
  "email": "u10@example.com",
  "password": "Test1234"
}
```

- Get users

```
query GetUsers{
  users{
    id
    email
    firstName
    lastName
    isActive
  }
}
```

- Test protected auth
```
query ProtectedAuth{
  protectedAuth{
    id
    email
  }
}
```

```
{
  "Authorization": "Bearer Access_token"
}
```


 - The `--run-syncdb` option helps to synchronize the database tables with the current state of your models without relying on the migration history.
 - `./manage.py migrate --run-syncdb`

 ### SQLite commands
 - Open database shell `sqlite3 db.sqlite3`

```
 .tables
 .schema account_user
 .mode column
 .headers on
 SELECT * FROM account_user;
 .exit
```


### Create credentials
 - for accessing Google Drive API, you need to follow these steps:
 - Go to the Google Cloud Console: Visit the Google Cloud Console. You may need to sign in with your Google account.
 - Create a new project (if necessary): If you don't have a project yet, create one by clicking on the project drop-down menu at the top of the page and selecting "New Project". Follow the prompts to set up your project.
 - Enable the Google Drive API: In the left sidebar menu, navigate to "APIs & Services" > "Dashboard". Click on the "+ ENABLE APIS AND SERVICES" button. Search for "Google Drive API", select it, and click "Enable".
 - Create credentials: In the left sidebar menu, navigate to "APIs & Services" > "Credentials". Click on "Create credentials" and select "Service account".

 - Fill out the form:
    - Service account name: Give your service account a name.
    - Role: Choose the role based on what access you need. For Google Drive, the role should have sufficient permissions like "Editor" or "Owner".
    - Key type: Choose "JSON" as the key type.
    - Create: Click the "Create" button. This will download a JSON file containing your credentials. Keep this file secure, as it contains sensitive information.
- Share folders or files (optional): If you want to upload files to specific folders or access specific files, make sure to share those folders/files with the email address associated with the service account.

### Test
 - Running test on the backend `pytest`
 - In Django and GraphQL projects, testing plays a crucial role in ensuring the correctness, reliability, and performance of your application. Here are some guidelines on what to test and what to avoid in Django and GraphQL projects:

#### What to Test:
 - GraphQL Queries and Mutations:
  Test individual GraphQL queries and mutations to ensure they return the expected data and handle input parameters correctly.
  Verify that GraphQL resolvers (functions that resolve GraphQL queries) return the correct data based on the schema definition.
 - Schema Integrity:
  Validate that the GraphQL schema is correctly defined and adheres to your application's data model.
  Ensure that schema changes are properly tested to avoid breaking existing queries or mutations.
 - Data Fetching:
  Test data fetching logic to verify that data is retrieved from the database or external sources (if applicable) accurately.
 - Authentication and Authorization:
  Test authentication and authorization mechanisms to ensure that only authorized users can access specific GraphQL operations.
  Validate error handling for unauthorized access attempts.
 - Edge Cases and Error Handling:
  Include tests for edge cases and error scenarios, such as invalid input, missing data, or unexpected behaviors.
  Verify error messages and status codes returned by GraphQL endpoints.
 - Performance Testing:
  Conduct performance tests to evaluate the efficiency of GraphQL queries and mutations, especially for complex or nested requests.
  Identify and optimize slow-performing queries or resolvers.
 - Integration Testing:
  Perform integration tests to simulate real-world interactions between different parts of your application, including Django models, GraphQL resolvers, and client-side components.
  Data Integrity and Validations:
  Test data validations and integrity constraints enforced by Django models and GraphQL schema.
  Ensure that database operations triggered by GraphQL mutations maintain data consistency.

#### What to Avoid:
 - Overlapping Test Coverage:
  Avoid duplicating test scenarios across different test cases. Instead, focus on testing unique functionality and edge cases.
 - Testing Django Core Features:
  Django's built-in features (e.g., ORM, view functions) are extensively tested by the Django framework itself. Avoid duplicating tests for Django's core functionality unless you're extending or customizing these features significantly.
 - Overly Granular Tests:
  While unit tests are valuable, avoid making tests overly granular, especially for GraphQL resolvers. Instead, consider testing related functionalities together in integration tests.
 - Testing External Libraries:
  Limit testing of external GraphQL libraries (e.g., Graphene) to ensure that they work as expected with your Django application. Focus on testing your application's specific use cases and business logic.
 - Relying Solely on Unit Tests:
  While unit tests are essential for isolated components, prioritize integration tests that cover end-to-end scenarios involving Django models, GraphQL resolvers, and client interactions.
 - Neglecting Test Coverage:
  Avoid neglecting critical parts of your application, such as authentication, authorization, and error handling, in your test suite. Aim for comprehensive test coverage to minimize bugs and regressions.
 - Hard-Coded Test Data:
  Refrain from using hard-coded test data that might become outdated or inconsistent over time. Instead, leverage fixtures or factories to generate realistic and reproducible test data.
 - Ignoring Performance Testing:
  GraphQL APIs can introduce performance bottlenecks, especially with complex queries or nested data fetching. Don't overlook performance testing to optimize query execution times and server responsiveness.

### References
 - Pytest - https://github.com/rodrigocardosodev/Django-GraphQL-Example/blob/master/post/tests/tests_post.py
-