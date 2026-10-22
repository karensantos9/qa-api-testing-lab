# Test Cases - Users API

## POST /users

### TC-USER-001 - Criar usuário com dados válidos

**Objetivo:**  
Validar a criação de um usuário com dados válidos.

**Request:**

```json
{
  "name": "Karen Teste",
  "email": "teste@example.com",
  "password": "123456",
  "role": "user"
}
```

**Resultado esperado:**
- Status code: `201 Created`
- Usuário criado com sucesso
- A senha não deve ser retornada na resposta

**Resultado:**  Pass

---

### TC-USER-002 - Nome com menos de 2 caracteres

**Objetivo:**  
Validar a regra de tamanho mínimo do nome.

**Request:**

```json
{
  "name": "A",
  "email": "teste2@example.com",
  "password": "123456",
  "role": "user"
}
```

**Resultado esperado:**
- Status code: `422 Unprocessable Entity`
- Usuário não deve ser criado

**Resultado:**  Pass

---

### TC-USER-003 - E-mail inválido

**Objetivo:**  
Validar a rejeição de e-mail em formato inválido.

**Request:**

```json
{
  "name": "Karen",
  "email": "email-invalido",
  "password": "123456",
  "role": "user"
}
```

**Resultado esperado:**
- Status code: `422 Unprocessable Entity`
- Usuário não deve ser criado

**Resultado:**  Pass

---

### TC-USER-004 - Senha com menos de 6 caracteres

**Objetivo:**  
Validar o tamanho mínimo da senha.

**Request:**

```json
{
  "name": "Karen",
  "email": "teste3@example.com",
  "password": "123",
  "role": "user"
}
```

**Resultado esperado:**
- Status code: `422 Unprocessable Entity`
- Usuário não deve ser criado

**Resultado:**  Pass

---

### TC-USER-005 - Role inválida

**Objetivo:**  
Validar que apenas as roles permitidas sejam aceitas.

**Request:**

```json
{
  "name": "Karen",
  "email": "teste4@example.com",
  "password": "123456",
  "role": "admin123"
}
```

**Resultado esperado:**
- Status code: `422 Unprocessable Entity`
- Usuário não deve ser criado

**Resultado:**  Pass

---

### TC-USER-006 - E-mail duplicado

**Objetivo:**  
Validar que não seja possível cadastrar dois usuários com o mesmo e-mail.

**Request:**

Utilizar os mesmos dados de um usuário já cadastrado.

**Resultado esperado:**
- Status code: `409 Conflict`
- Mensagem: `Email already registered`
- Usuário duplicado não deve ser criado

**Resultado obtido:**

```json
{
  "detail": "Email already registered"
}
```

**Resultado:**  Pass

---

### TC-USER-007 - Campo obrigatório ausente

**Objetivo:**  
Validar a obrigatoriedade dos campos necessários para criação do usuário.

**Request:**

```json
{
  "email": "teste7@example.com",
  "password": "123456",
  "role": "user"
}
```

**Resultado esperado:**
- Status code: `422 Unprocessable Entity`
- Usuário não deve ser criado

**Resultado:**  Pass

---

## GET /users

### TC-USER-008 - Listar usuários

**Objetivo:**

Validar a listagem dos usuários cadastrados.

**Request:**

```http
GET /users
```

**Resultado esperado:**

- Status code: `200 OK`
- A resposta deve ser uma lista de usuários
- Cada usuário deve conter `id`, `name`, `email` e `role`
- A senha não deve ser retornada na resposta

**Resultado:** ✅ Pass

---

## GET /users/{user_id}

### TC-USER-009 - Buscar usuário existente

**Objetivo:**

Validar a consulta de um usuário existente pelo ID.

**Request:**

```http
GET /users/1
```

**Resultado esperado:**

- Status code: `200 OK`
- Usuário deve ser retornado com sucesso
- A resposta deve conter `id`, `name`, `email` e `role`
- A senha não deve ser retornada na resposta

**Resultado:** ✅ Pass

---

### TC-USER-010 - Buscar usuário inexistente

**Objetivo:**

Validar o comportamento da API ao consultar um usuário que não existe.

**Request:**

```http
GET /users/99999
```

**Resultado esperado:**

- Status code: `404 Not Found`
- Mensagem: `User not found`
- Usuário não deve ser retornado

**Resultado obtido:**

```json
{
  "detail": "User not found"
}
```

**Resultado:** ✅ Pass

---

## PUT /users/{user_id}

### TC-USER-011 - Atualizar usuário com dados válidos

**Objetivo:**

Validar a atualização de um usuário existente com dados válidos.

**Request:**

```http
PUT /users/1
```

```json
{
  "name": "Postman Updated User",
  "email": "updated@example.com",
  "role": "admin"
}
```

**Resultado esperado:**

- Status code: `200 OK`
- Usuário deve ser atualizado com sucesso
- Os dados retornados devem corresponder aos novos valores
- A senha não deve ser retornada na resposta

**Resultado:** ✅ Pass

---

### TC-USER-012 - Atualizar usuário inexistente

**Objetivo:**

Validar o comportamento da API ao tentar atualizar um usuário que não existe.

**Request:**

```http
PUT /users/99999
```

```json
{
  "name": "User Not Found",
  "email": "notfound@example.com",
  "role": "user"
}
```

**Resultado esperado:**

- Status code: `404 Not Found`
- Mensagem: `User not found`
- Usuário não deve ser atualizado

**Resultado obtido:**

```json
{
  "detail": "User not found"
}
```

**Resultado:** ✅ Pass

---

### TC-USER-013 - Atualizar com e-mail duplicado

**Objetivo:**

Validar que não seja possível atualizar um usuário utilizando um e-mail já pertencente a outro usuário.

**Request:**

```http
PUT /users/1
```

```json
{
  "name": "Trying Duplicate Email",
  "email": "postman@example.com",
  "role": "user"
}
```

**Resultado esperado:**

- Status code: `409 Conflict`
- Mensagem: `Email already registered`
- Usuário não deve ser atualizado

**Resultado obtido:**

```json
{
  "detail": "Email already registered"
}
```

**Resultado:** ✅ Pass

---

### TC-USER-014 - Atualizar com nome inválido

**Objetivo:**

Validar a regra de tamanho mínimo do nome durante a atualização.

**Request:**

```http
PUT /users/1
```

```json
{
  "name": "A",
  "email": "valid-update-name@example.com",
  "role": "user"
}
```

**Resultado esperado:**

- Status code: `422 Unprocessable Entity`
- O erro deve identificar o campo `name`
- Usuário não deve ser atualizado

**Resultado:** ✅ Pass

---

### TC-USER-015 - Atualizar com e-mail inválido

**Objetivo:**

Validar a rejeição de e-mail em formato inválido durante a atualização.

**Request:**

```http
PUT /users/1
```

```json
{
  "name": "Valid Update",
  "email": "email-invalido",
  "role": "user"
}
```

**Resultado esperado:**

- Status code: `422 Unprocessable Entity`
- O erro deve identificar o campo `email`
- Usuário não deve ser atualizado

**Resultado:** ✅ Pass

---

### TC-USER-016 - Atualizar com role inválida

**Objetivo:**

Validar que apenas as roles permitidas sejam aceitas durante a atualização.

**Request:**

```http
PUT /users/1
```

```json
{
  "name": "Valid Update",
  "email": "valid-role-update@example.com",
  "role": "admin123"
}
```

**Resultado esperado:**

- Status code: `422 Unprocessable Entity`
- O erro deve identificar o campo `role`
- Usuário não deve ser atualizado

**Resultado:** ✅ Pass


---

## DELETE /users/{user_id}

### TC-USER-017 - Excluir usuário existente

**Objetivo:**

Validar a exclusão de um usuário existente.

**Request:**

```http
DELETE /users/{user_id}
```

**Resultado esperado:**

- Status code: `204 No Content`
- Usuário deve ser excluído com sucesso
- A resposta não deve possuir conteúdo

**Resultado:** ✅ Pass

---

### TC-USER-018 - Excluir usuário inexistente

**Objetivo:**

Validar o comportamento da API ao tentar excluir um usuário que não existe.

**Request:**

```http
DELETE /users/99999
```

**Resultado esperado:**

- Status code: `404 Not Found`
- Mensagem: `User not found`
- Nenhum usuário deve ser excluído

**Resultado obtido:**

```json
{
  "detail": "User not found"
}
```

**Resultado:** ✅ Pass