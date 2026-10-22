# Test Cases - Products API

## POST /products

### TC-PRODUCT-001 - Criar produto com dados válidos

**Objetivo:**

Validar a criação de um produto com dados válidos.

**Request:**

```json
{
  "name": "Postman Notebook",
  "price": 3500,
  "stock": 10
}
```

**Resultado esperado:**

- Status code: `201 Created`
- Produto criado com sucesso
- A resposta deve conter `id`, `name`, `price` e `stock`

**Resultado:** ✅ Pass

---

### TC-PRODUCT-002 - Nome inválido

**Objetivo:**

Validar a rejeição de um produto com nome menor que 2 caracteres.

**Request:**

```json
{
  "name": "A",
  "price": 100,
  "stock": 10
}
```

**Resultado esperado:**

- Status code: `422 Unprocessable Entity`
- O erro deve identificar o campo `name`
- Produto não deve ser criado

**Resultado:** ✅ Pass

---

### TC-PRODUCT-003 - Preço igual a zero

**Objetivo:**

Validar que produtos não possam ser cadastrados com preço igual a zero.

**Request:**

```json
{
  "name": "Zero Price Product",
  "price": 0,
  "stock": 10
}
```

**Resultado esperado:**

- Status code: `422 Unprocessable Entity`
- O erro deve identificar o campo `price`
- Produto não deve ser criado

**Resultado:** ✅ Pass

---

### TC-PRODUCT-004 - Preço negativo

**Objetivo:**

Validar que produtos não possam ser cadastrados com preço negativo.

**Request:**

```json
{
  "name": "Negative Price Product",
  "price": -100,
  "stock": 10
}
```

**Resultado esperado:**

- Status code: `422 Unprocessable Entity`
- O erro deve identificar o campo `price`
- Produto não deve ser criado

**Resultado:** ✅ Pass

---

### TC-PRODUCT-005 - Estoque negativo

**Objetivo:**

Validar que produtos não possam ser cadastrados com estoque negativo.

**Request:**

```json
{
  "name": "Negative Stock Product",
  "price": 100,
  "stock": -1
}
```

**Resultado esperado:**

- Status code: `422 Unprocessable Entity`
- O erro deve identificar o campo `stock`
- Produto não deve ser criado

**Resultado:** ✅ Pass

---

### TC-PRODUCT-006 - Nome duplicado

**Objetivo:**

Validar que não seja possível cadastrar dois produtos com o mesmo nome.

**Request:**

Utilizar o mesmo nome de um produto já cadastrado.

```json
{
  "name": "Postman Notebook",
  "price": 4000,
  "stock": 5
}
```

**Resultado esperado:**

- Status code: `409 Conflict`
- Mensagem: `Product name already registered`
- Produto duplicado não deve ser criado

**Resultado obtido:**

```json
{
  "detail": "Product name already registered"
}
```

**Resultado:** ✅ Pass

---

## GET /products

### TC-PRODUCT-007 - Listar produtos

**Objetivo:**

Validar a listagem dos produtos cadastrados.

**Request:**

```http
GET /products
```

**Resultado esperado:**

- Status code: `200 OK`
- A resposta deve ser uma lista de produtos
- Cada produto deve conter `id`, `name`, `price` e `stock`

**Resultado:** ✅ Pass

---

## GET /products/{product_id}

### TC-PRODUCT-008 - Buscar produto existente

**Objetivo:**

Validar a consulta de um produto existente pelo ID.

**Request:**

```http
GET /products/{product_id}
```

**Resultado esperado:**

- Status code: `200 OK`
- Produto deve ser retornado com sucesso
- A resposta deve conter `id`, `name`, `price` e `stock`

**Resultado:** ✅ Pass

---

### TC-PRODUCT-009 - Buscar produto inexistente

**Objetivo:**

Validar o comportamento da API ao consultar um produto que não existe.

**Request:**

```http
GET /products/99999
```

**Resultado esperado:**

- Status code: `404 Not Found`
- Mensagem: `Product not found`
- Produto não deve ser retornado

**Resultado obtido:**

```json
{
  "detail": "Product not found"
}
```

**Resultado:** ✅ Pass

---

## PUT /products/{product_id}

### TC-PRODUCT-010 - Atualizar produto com dados válidos

**Objetivo:**

Validar a atualização de um produto existente com dados válidos.

**Request:**

```http
PUT /products/{product_id}
```

```json
{
  "name": "Postman Notebook Updated",
  "price": 3200,
  "stock": 15
}
```

**Resultado esperado:**

- Status code: `200 OK`
- Produto deve ser atualizado com sucesso
- Os dados retornados devem corresponder aos novos valores

**Resultado:** ✅ Pass

---

### TC-PRODUCT-011 - Atualizar produto inexistente

**Objetivo:**

Validar o comportamento da API ao tentar atualizar um produto que não existe.

**Request:**

```http
PUT /products/99999
```

```json
{
  "name": "Product Not Found",
  "price": 100,
  "stock": 10
}
```

**Resultado esperado:**

- Status code: `404 Not Found`
- Mensagem: `Product not found`
- Produto não deve ser atualizado

**Resultado obtido:**

```json
{
  "detail": "Product not found"
}
```

**Resultado:** ✅ Pass

---

### TC-PRODUCT-012 - Atualizar com nome duplicado

**Objetivo:**

Validar que não seja possível atualizar um produto utilizando o nome de outro produto já cadastrado.

**Request:**

```http
PUT /products/{product_id}
```

Utilizar no campo `name` o nome de outro produto existente.

```json
{
  "name": "Mouse",
  "price": 200,
  "stock": 10
}
```

**Resultado esperado:**

- Status code: `409 Conflict`
- Mensagem: `Product name already registered`
- Produto não deve ser atualizado

**Resultado obtido:**

```json
{
  "detail": "Product name already registered"
}
```

**Resultado:** ✅ Pass

---

### TC-PRODUCT-013 - Atualizar com nome inválido

**Objetivo:**

Validar a regra de tamanho mínimo do nome durante a atualização.

**Request:**

```http
PUT /products/{product_id}
```

```json
{
  "name": "A",
  "price": 100,
  "stock": 10
}
```

**Resultado esperado:**

- Status code: `422 Unprocessable Entity`
- O erro deve identificar o campo `name`
- Produto não deve ser atualizado

**Resultado:** ✅ Pass

---

### TC-PRODUCT-014 - Atualizar com preço inválido

**Objetivo:**

Validar que um produto não possa ser atualizado com preço igual a zero.

**Request:**

```http
PUT /products/{product_id}
```

```json
{
  "name": "Valid Product",
  "price": 0,
  "stock": 10
}
```

**Resultado esperado:**

- Status code: `422 Unprocessable Entity`
- O erro deve identificar o campo `price`
- Produto não deve ser atualizado

**Resultado:** ✅ Pass

---

### TC-PRODUCT-015 - Atualizar com estoque inválido

**Objetivo:**

Validar que um produto não possa ser atualizado com estoque negativo.

**Request:**

```http
PUT /products/{product_id}
```

```json
{
  "name": "Valid Product",
  "price": 100,
  "stock": -1
}
```

**Resultado esperado:**

- Status code: `422 Unprocessable Entity`
- O erro deve identificar o campo `stock`
- Produto não deve ser atualizado

**Resultado:** ✅ Pass

---

## DELETE /products/{product_id}

### TC-PRODUCT-016 - Excluir produto existente

**Objetivo:**

Validar a exclusão de um produto existente.

**Request:**

```http
DELETE /products/{product_id}
```

**Resultado esperado:**

- Status code: `204 No Content`
- Produto deve ser excluído com sucesso
- A resposta não deve possuir conteúdo

**Resultado:** ✅ Pass

---

### TC-PRODUCT-017 - Excluir produto inexistente

**Objetivo:**

Validar o comportamento da API ao tentar excluir um produto que não existe.

**Request:**

```http
DELETE /products/99999
```

**Resultado esperado:**

- Status code: `404 Not Found`
- Mensagem: `Product not found`
- Nenhum produto deve ser excluído

**Resultado obtido:**

```json
{
  "detail": "Product not found"
}
```

**Resultado:** ✅ Pass