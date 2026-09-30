# API Contracts

## POST /users

### Request

```json
{
  "name": "Karen Souza",
  "email": "karen@example.com",
  "password": "Password123"
}

### Expected Response
{
  "id": 1,
  "name": "Karen Souza",
  "email": "karen@example.com"
}