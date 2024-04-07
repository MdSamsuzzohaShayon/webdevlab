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