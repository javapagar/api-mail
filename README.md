# api-mail
api for sends email

## Stack
* Django
* DRF

## Environment variables
* DEFAULT_FROM_EMAIL
* EMAIL_BACKEND
* EMAIL_HOST
* EMAIL_PORT
* EMAIL_USE_TLS
* EMAIL_HOST_USER
* EMAIL_HOST_PASSWORD

## Security
We must create a user for login our API. With taht user and password we can generate
a Token access and token refresh with 
endpoint:

```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "", "password": ""}' \
  http://localhost:8000/api/token/
```

We can use the returned access token to prove authentication for a protected view
```
curl \
  -X POST \
  -H "Authorization: Bearer <token>" \
  -d '{
    "name":"",
    "subject": "Test API",
    "from_email": "",
    "to_email":"",
    "message": "Test from API"
    }'
  http://localhost:8000/api/send-mail
  ```