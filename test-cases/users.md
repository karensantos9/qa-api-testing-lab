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