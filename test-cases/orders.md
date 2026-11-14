# Testes de API — Orders

## 1. Objetivo

Documentar os testes funcionais e de validação realizados no módulo de pedidos (*Orders*) da Sales API.

O objetivo é verificar a criação, consulta, atualização e exclusão de pedidos, além das regras de negócio relacionadas a produtos, quantidades, estoque e autenticação.

## 2. Endpoint

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/orders` | Criar pedido |
| GET | `/orders` | Listar pedidos do usuário autenticado |
| GET | `/orders/{order_id}` | Consultar pedido por ID |
| PUT | `/orders/{order_id}` | Atualizar pedido |
| DELETE | `/orders/{order_id}` | Excluir pedido |

**Autenticação:** todos os endpoints exigem autenticação via Bearer Token (JWT).

## 3. Regras de negócio validadas

- Um pedido deve possuir pelo menos um item.
- Cada item deve referenciar um produto existente.
- A quantidade de cada item deve ser maior ou igual a 1.
- Não é permitido adicionar o mesmo produto mais de uma vez no mesmo pedido.
- O estoque deve ser suficiente para atender à quantidade solicitada.
- O total do pedido deve corresponder à soma dos subtotais dos itens.
- O preço unitário utilizado no pedido deve corresponder ao preço do produto no momento da operação.
- Cada usuário só pode consultar, atualizar ou excluir seus próprios pedidos.
- A exclusão de um pedido deve restaurar as quantidades correspondentes ao estoque.

## 4. Casos de teste

### 4.1. Criação de pedidos — POST `/orders`

| ID | Cenário | Resultado esperado | Status |
|---|---|---|---|
| ORD-001 | Criar pedido com dados válidos | Pedido criado com os dados e total corretos | 201 |
| ORD-002 | Criar pedido sem itens | Retornar erro de validação | 422 |
| ORD-003 | Criar pedido com produto inexistente | Retornar mensagem de produto não encontrado | 404 |
| ORD-004 | Criar pedido com quantidade zero | Retornar erro de validação | 422 |
| ORD-005 | Criar pedido com quantidade negativa | Retornar erro de validação | 422 |
| ORD-006 | Criar pedido com quantidade superior ao estoque | Retornar mensagem de estoque insuficiente | 400 |
| ORD-007 | Criar pedido com produto duplicado | Retornar mensagem informando que produtos duplicados não são permitidos | 422 |

### 4.2. Consulta de pedidos — GET `/orders`

| ID | Cenário | Resultado esperado | Status |
|---|---|---|---|
| ORD-008 | Listar pedidos do usuário autenticado | Retornar lista de pedidos | 200 |
| ORD-009 | Consultar pedido existente | Retornar os dados completos do pedido | 200 |
| ORD-010 | Consultar pedido inexistente | Retornar mensagem de pedido não encontrado | 404 |

### 4.3. Atualização de pedidos — PUT `/orders/{order_id}`

| ID | Cenário | Resultado esperado | Status |
|---|---|---|---|
| ORD-011 | Atualizar pedido com dados válidos | Atualizar os itens e recalcular o total | 200 |
| ORD-012 | Atualizar pedido inexistente | Retornar mensagem de pedido não encontrado | 404 |
| ORD-013 | Atualizar pedido com produto inexistente | Retornar mensagem de produto não encontrado | 404 |
| ORD-014 | Atualizar pedido com quantidade superior ao estoque disponível | Retornar mensagem de estoque insuficiente | 400 |

### 4.4. Exclusão de pedidos — DELETE `/orders/{order_id}`

| ID | Cenário | Resultado esperado | Status |
|---|---|---|---|
| ORD-015 | Excluir pedido existente | Excluir pedido com sucesso, sem conteúdo na resposta | 204 |
| ORD-016 | Excluir pedido inexistente | Retornar mensagem de pedido não encontrado | 404 |

### 4.5. Autenticação

| ID | Cenário | Resultado esperado | Status |
|---|---|---|---|
| ORD-017 | Consultar pedidos sem token | Retornar mensagem de autenticação ausente | 401 |
| ORD-018 | Consultar pedidos com token inválido | Retornar mensagem de token inválido ou expirado | 401 |

## 5. Resultados da execução

Os testes foram executados utilizando o Postman, com scripts de validação em JavaScript na aba **Scripts > Post-response**.

| Indicador | Quantidade |
|---|---:|
| Total de cenários documentados | 18 |
| Cenários executados | 17 |
| Cenários aprovados | 17 |
| Cenários não executados | 1 |
| Cenários com falha | 0 |

**Observação:** o cenário ORD-018 (token inválido) foi documentado, mas não foi executado nesta rodada. Portanto, não deve ser contabilizado como aprovado.

## 6. Evidências e validações realizadas

Durante a execução, foram verificadas as seguintes condições:

- Retorno dos códigos HTTP esperados.
- Estrutura dos objetos JSON retornados pela API.
- Presença dos campos obrigatórios dos pedidos e itens.
- Correspondência entre o total do pedido e a soma dos subtotais.
- Tratamento de produtos inexistentes.
- Validação de quantidades inválidas.
- Tratamento de estoque insuficiente.
- Bloqueio de produtos duplicados.
- Tratamento de pedidos inexistentes.
- Proteção dos endpoints por autenticação.
- Resposta adequada para requisições sem token.

## 7. Conclusão

O módulo Orders apresentou resultados satisfatórios nos 17 cenários executados. As funcionalidades de criação, consulta, atualização e exclusão de pedidos foram validadas, assim como as principais regras de negócio relacionadas a produtos, quantidades e estoque.

Os scripts do Postman passaram em todos os cenários executados. Permanece pendente a execução do teste de autenticação com token inválido (ORD-018).

A documentação registra os resultados desta rodada e poderá ser atualizada conforme novos cenários forem implementados e executados.