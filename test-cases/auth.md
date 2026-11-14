# Auth – Casos de Teste

## 1. Objetivo

Validar o funcionamento da autenticação da Sales API, verificando o login de usuários, a geração de tokens JWT e o controle de acesso aos endpoints protegidos.

Os testes contemplam cenários positivos e negativos, incluindo credenciais inválidas, campos obrigatórios ausentes e tentativas de acesso sem autenticação.

## 2. Endpoints testados

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/auth/login` | Realizar autenticação e gerar token JWT |
| GET | `/auth/me` | Consultar os dados do usuário autenticado |

## 3. Casos de teste

### POST /auth/login

#### TC-AUTH-001 – Login com credenciais válidas

**Objetivo:** Verificar se um usuário consegue realizar login utilizando e-mail e senha corretos.

**Pré-condições:**
- Usuário previamente cadastrado na API.
- Credenciais válidas.

**Dados de entrada:**
```json
{
    "email": "karen.souza12312@gmail.com",
    "password": "senha123"
}
```

**Resultado esperado:**
- Status HTTP `200 OK`.
- Resposta contendo `access_token`.
- Campo `token_type` com valor `bearer`.
- Token JWT gerado corretamente.
- Senha e hash não devem ser expostos na resposta.

**Resultado obtido:** Conforme esperado.

**Status:** Aprovado.

---

#### TC-AUTH-002 – Login com senha incorreta

**Objetivo:** Verificar se a API rejeita a autenticação quando a senha informada está incorreta.

**Pré-condições:**
- Usuário previamente cadastrado.
- E-mail existente.

**Dados de entrada:**
```json
{
    "email": "karen.souza12312@gmail.com",
    "password": "senhaErrada123"
}
```

**Resultado esperado:**
- Status HTTP `401 Unauthorized`.
- Mensagem: `Incorrect email or password`.
- Nenhum token deve ser gerado.

**Resultado obtido:** Conforme esperado.

**Status:** Aprovado.

---

#### TC-AUTH-003 – Login com usuário inexistente

**Objetivo:** Verificar se a API rejeita a autenticação de um usuário não cadastrado.

**Dados de entrada:**
```json
{
    "email": "usuario.inexistente@teste.com",
    "password": "senha123"
}
```

**Resultado esperado:**
- Status HTTP `401 Unauthorized`.
- Mensagem: `Incorrect email or password`.
- A API não deve revelar se o e-mail está cadastrado.

**Resultado obtido:** Conforme esperado.

**Status:** Aprovado.

---

#### TC-AUTH-004 – Login sem e-mail

**Objetivo:** Verificar se a API identifica a ausência do campo obrigatório `email`.

**Dados de entrada:**
```json
{
    "password": "senha123"
}
```

**Resultado esperado:**
- Status HTTP `422 Unprocessable Entity`.
- Resposta identificando o campo `email` como obrigatório.
- Mensagem: `Field required`.

**Resultado obtido:** Conforme esperado.

**Status:** Aprovado.

---

#### TC-AUTH-005 – Login sem senha

**Objetivo:** Verificar se a API identifica a ausência do campo obrigatório `password`.

**Dados de entrada:**
```json
{
    "email": "karen.souza12312@gmail.com"
}
```

**Resultado esperado:**
- Status HTTP `422 Unprocessable Entity`.
- Resposta identificando o campo `password` como obrigatório.
- Mensagem: `Field required`.

**Resultado obtido:** Conforme esperado.

**Status:** Aprovado.

### GET /auth/me

#### TC-AUTH-006 – Consultar usuário autenticado com token válido

**Objetivo:** Verificar se a API permite o acesso ao endpoint protegido quando um token JWT válido é informado.

**Pré-condições:**
- Usuário cadastrado.
- Login realizado com sucesso.
- Token JWT válido gerado pela API.

**Autorização:**
- Tipo: Bearer Token.
- Token: JWT obtido no login.

**Resultado esperado:**
- Status HTTP `200 OK`.
- Retorno dos dados do usuário autenticado.
- Presença dos campos `id`, `name`, `email` e `role`.
- Senha e hash não devem ser expostos.

**Resultado obtido:** Conforme esperado.

**Status:** Aprovado.

---

#### TC-AUTH-007 – Consultar usuário sem token

**Objetivo:** Verificar se a API bloqueia o acesso ao endpoint protegido quando nenhuma credencial de autenticação é fornecida.

**Pré-condições:**
- Endpoint `/auth/me` disponível.
- Requisição sem autenticação.

**Resultado esperado:**
- Status HTTP `401 Unauthorized`.
- Mensagem: `Not authenticated`.
- Acesso negado.

**Resultado obtido:** Conforme esperado.

**Status:** Aprovado.

---

#### TC-AUTH-008 – Consultar usuário com token inválido

**Objetivo:** Verificar se a API rejeita tokens inválidos ou adulterados.

**Pré-condições:**
- Endpoint `/auth/me` disponível.
- Token JWT inválido.

**Autorização:**
- Tipo: Bearer Token.
- Token: `token-invalido-123`.

**Resultado esperado:**
- Status HTTP `401 Unauthorized`.
- Mensagem: `Invalid or expired token`.
- Acesso negado.

**Resultado obtido:** Conforme esperado.

**Status:** Aprovado.

## 4. Resumo dos resultados

| ID | Cenário | Resultado |
|---|---|---|
| TC-AUTH-001 | Login com credenciais válidas | Aprovado |
| TC-AUTH-002 | Login com senha incorreta | Aprovado |
| TC-AUTH-003 | Login com usuário inexistente | Aprovado |
| TC-AUTH-004 | Login sem e-mail | Aprovado |
| TC-AUTH-005 | Login sem senha | Aprovado |
| TC-AUTH-006 | Acesso com token válido | Aprovado |
| TC-AUTH-007 | Acesso sem token | Aprovado |
| TC-AUTH-008 | Acesso com token inválido | Aprovado |

**Total de casos de teste:** 8

**Aprovados:** 8

**Reprovados:** 0

**Taxa de aprovação:** 100%

## 5. Automação no Postman

Os oito cenários foram implementados e validados no Postman, utilizando scripts JavaScript na aba Post-response.

As validações automatizadas contemplam:

- Verificação dos códigos de status HTTP.
- Validação da estrutura das respostas.
- Verificação das mensagens de erro.
- Identificação de campos obrigatórios ausentes.
- Validação da geração do token JWT.
- Armazenamento do token em variável da coleção.
- Verificação de autenticação em endpoint protegido.
- Rejeição de tokens ausentes e inválidos.

O token gerado no cenário de login válido é armazenado na variável de coleção `access_token` e reutilizado na requisição de consulta do usuário autenticado.

## 6. Conclusão

Os testes realizados demonstraram que o módulo de autenticação apresenta o comportamento esperado nos cenários avaliados.

A API realiza a autenticação por e-mail e senha, gera tokens JWT para usuários autenticados e controla o acesso ao endpoint protegido `/auth/me`.

Também foram validadas as respostas para credenciais incorretas, usuários inexistentes, ausência de campos obrigatórios e utilização de tokens inválidos.

Todos os oito cenários foram aprovados nos testes manuais e nas validações automatizadas do Postman.