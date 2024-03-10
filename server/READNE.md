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
 - The `--run-syncdb` option helps to synchronize the database tables with the current state of your models without relying on the migration history.
 - `./manage.py migrate --run-syncdb`