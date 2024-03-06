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
      birth
    }
  }
}
```

```
{
  "email": "u1@example.com",
  "password": "Test1234",
  "firstName": "fn1",
  "lastName": "ln1",
  "birth": "2024-03-06T11:26:12.306Z"
}
```