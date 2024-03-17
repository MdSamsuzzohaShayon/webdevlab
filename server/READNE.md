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